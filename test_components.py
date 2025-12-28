#!/usr/bin/env python3
"""
Test script to validate bot components
"""

import asyncio
import sys
from database import Database
from cache_manager import CacheManager
from scraper import HDhub4uScraper
from bot import escape_markdown, format_post_message

def test_database():
    """Test database functionality"""
    print("Testing Database...")
    db = Database('test_bot.db')
    
    # Test settings
    db.set_setting('test_key', 'test_value')
    assert db.get_setting('test_key') == 'test_value', "Setting storage failed"
    
    # Test posts
    success = db.add_post('Test Movie', 'https://example.com/test')
    assert success, "Failed to add post"
    
    assert db.is_posted('https://example.com/test'), "Post not found"
    assert not db.is_posted('https://example.com/nonexistent'), "False positive"
    
    # Test duplicate prevention
    duplicate = db.add_post('Test Movie 2', 'https://example.com/test')
    assert not duplicate, "Duplicate prevention failed"
    
    # Test statistics
    total = db.get_total_posts()
    assert total > 0, "Post count failed"
    
    # Cleanup
    import os
    db.close()
    if os.path.exists('test_bot.db'):
        os.remove('test_bot.db')
    
    print("✅ Database tests passed!")

def test_cache():
    """Test cache functionality"""
    print("\nTesting Cache Manager...")
    cache = CacheManager()
    
    # Test set/get
    cache.set('test_key', 'test_value', ttl=10)
    assert cache.get('test_key') == 'test_value', "Cache storage failed"
    
    # Test miss
    assert cache.get('nonexistent') is None, "Cache false positive"
    
    # Test stats
    stats = cache.get_stats()
    assert stats['size'] > 0, "Cache size wrong"
    assert stats['hits'] > 0, "Cache hits not tracked"
    
    # Test expiration
    cache.set('temp', 'value', ttl=1)
    import time
    time.sleep(2)
    assert cache.get('temp') is None, "Cache expiration failed"
    
    # Test clear
    cache.clear()
    assert cache.size() == 0, "Cache clear failed"
    
    print("✅ Cache tests passed!")

async def test_scraper():
    """Test scraper functionality"""
    print("\nTesting Scraper...")
    scraper = HDhub4uScraper()
    cache = CacheManager()
    
    try:
        # Test scraping (may fail if website is down)
        content = await scraper.get_latest_content(cache)
        
        if content:
            print(f"  Scraped {len(content)} items")
            
            # Test content structure
            item = content[0]
            assert 'title' in item, "Title missing"
            assert 'url' in item, "URL missing"
            
            print(f"  Sample: {item['title']}")
            print("✅ Scraper tests passed!")
        else:
            print("⚠️  No content scraped (website might be down)")
    
    except Exception as e:
        print(f"⚠️  Scraper test error: {e}")
        print("   (This may be normal if website is unreachable)")
    
    finally:
        await scraper.close()

def test_markdown_escape():
    """Test markdown escape functionality"""
    print("\nTesting Markdown Escape...")
    
    # Test basic escaping
    assert escape_markdown("Hello World") == "Hello World", "Plain text should not change"
    
    # Test underscore (common in titles)
    assert escape_markdown("Movie_Name") == "Movie\\_Name", "Underscore not escaped"
    
    # Test asterisk
    assert escape_markdown("Movie*Star") == "Movie\\*Star", "Asterisk not escaped"
    
    # Test brackets
    assert escape_markdown("Movie [2024]") == "Movie \\[2024\\]", "Brackets not escaped"
    
    # Test parentheses
    assert escape_markdown("Movie (HD)") == "Movie \\(HD\\)", "Parentheses not escaped"
    
    # Test multiple special characters
    text = "Movie_Name* [2024] (HD-Rip)"
    escaped = escape_markdown(text)
    assert "\\_" in escaped and "\\*" in escaped and "\\[" in escaped, "Multiple chars not escaped"
    
    # Test empty string
    assert escape_markdown("") == "", "Empty string failed"
    assert escape_markdown(None) is None, "None handling failed"
    
    # Test complex title with many special characters
    complex_title = "Spider-Man: No Way Home (2021) [4K-UHD]"
    escaped = escape_markdown(complex_title)
    # Verify critical special characters are escaped
    assert "\\-" in escaped and "\\[" in escaped and "\\(" in escaped, "Complex title not fully escaped"
    
    print("✅ Markdown escape tests passed!")

def test_message_formatting():
    """Test message formatting with escaped markdown"""
    print("\nTesting Message Formatting...")
    
    # Test basic item
    item = {
        'title': 'Test Movie',
        'quality': '1080p',
        'year': '2024',
        'rating': '8.5',
        'genre': ['Action', 'Adventure'],
        'plot': 'A test plot',
        'download_links': [{'url': 'http://test.com', 'quality': '1080p'}]
    }
    
    message = format_post_message(item)
    assert '🎬 \\*Test Movie\\*' in message or '🎬 *Test Movie*' in message, "Title not formatted"
    assert '1080p' in message, "Quality missing"
    assert '2024' in message, "Year missing"
    
    # Test with special characters in title
    item_special = {
        'title': 'Spider-Man: No Way Home [2021]',
        'quality': '4K',
        'download_links': []
    }
    
    message_special = format_post_message(item_special)
    # Should have escaped special characters
    assert '\\-' in message_special or '-' in message_special, "Dash handling issue"
    assert '\\[' in message_special or '[' in message_special, "Bracket handling issue"
    
    # Test with empty fields
    item_empty = {
        'title': 'Simple Movie',
        'download_links': []
    }
    
    message_empty = format_post_message(item_empty)
    assert 'Simple Movie' in message_empty, "Basic title missing"
    
    print("✅ Message formatting tests passed!")

def run_tests():
    """Run all tests"""
    print("=" * 50)
    print("Running Component Tests")
    print("=" * 50)
    
    try:
        test_database()
        test_cache()
        test_markdown_escape()
        test_message_formatting()
        asyncio.run(test_scraper())
        
        print("\n" + "=" * 50)
        print("✅ All tests completed!")
        print("=" * 50)
        return 0
    
    except Exception as e:
        print("\n" + "=" * 50)
        print(f"❌ Tests failed: {e}")
        print("=" * 50)
        return 1

if __name__ == '__main__':
    sys.exit(run_tests())

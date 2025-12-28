# Usage Guide - HDhub4u Telegram Auto-Post Bot

Complete guide on how to use and configure the bot.

## Table of Contents
1. [Initial Setup](#initial-setup)
2. [Basic Configuration](#basic-configuration)
3. [Admin Commands](#admin-commands)
4. [Auto-Posting](#auto-posting)
5. [Monitoring](#monitoring)
6. [Advanced Usage](#advanced-usage)
7. [Best Practices](#best-practices)
8. [FAQ](#faq)

---

## Initial Setup

### 1. Start the Bot

After deployment, find your bot on Telegram and start it:

```
/start
```

You'll see a welcome message with the current configuration and available commands.

### 2. Set Up Your Channel

First, configure the channel where content will be posted:

```
/setchannel @yourchannel
```

Or use channel ID:
```
/setchannel -1001234567890
```

**Important**: Make sure your bot is an administrator in the channel with "Post Messages" permission.

### 3. Configure Timer

Set how often the bot should post (in minutes):

```
/settimer 5
```

This sets posting every 5 minutes. You can use any value from 1 to 1440 (24 hours).

**Recommended intervals:**
- Testing: 10-15 minutes
- Production: 5-10 minutes
- Low activity: 30-60 minutes

---

## Basic Configuration

### Channel Setup

**Using Channel Username:**
```
/setchannel @mychannel
```

**Using Channel ID:**
```
/setchannel -1001234567890
```

To get your channel ID:
1. Forward a message from your channel to [@userinfobot](https://t.me/userinfobot)
2. It will show the channel ID

### Timer Configuration

```
/settimer [minutes]
```

Examples:
- `/settimer 5` - Post every 5 minutes
- `/settimer 15` - Post every 15 minutes
- `/settimer 60` - Post every hour

### Verify Configuration

Check current settings:
```
/status
```

This shows:
- Channel name/ID
- Timer interval
- Auto-posting status
- Total posts count
- Last post time

---

## Admin Commands

### Essential Commands

**Start Bot**
```
/start
```
Initialize bot and view welcome message with current configuration.

**Set Channel**
```
/setchannel @channelname
```
Configure target channel for posting.

**Set Timer**
```
/settimer 5
```
Set auto-post interval in minutes.

**Start Auto-Posting**
```
/start_autopost
```
Begin automatic content posting.

**Stop Auto-Posting**
```
/stop_autopost
```
Pause automatic posting (can be resumed later).

### Monitoring Commands

**View Status**
```
/status
```
Shows:
- Current configuration
- Channel name
- Timer setting
- Auto-post status
- Post statistics
- Last post time

**View Statistics**
```
/stats
```
Shows detailed statistics:
- Total posts all-time
- Posts today
- Unique content count
- Cache performance
- Database size

**View Post History**
```
/posted
```
Shows last 10 posts with titles and timestamps.

### Manual Control

**Force Post**
```
/force_post
```
Manually trigger a post immediately (bypasses timer).

Use this for:
- Testing the bot
- Posting urgent content
- Recovering from errors

---

## Auto-Posting

### Starting Auto-Posting

1. Ensure channel is configured:
   ```
   /setchannel @yourchannel
   ```

2. Set desired interval:
   ```
   /settimer 5
   ```

3. Start auto-posting:
   ```
   /start_autopost
   ```

4. Verify it's running:
   ```
   /status
   ```

### How Auto-Posting Works

1. **Scheduled Check**: Every X minutes (based on timer)
2. **Content Fetch**: Scrapes latest content from HDhub4u
3. **Duplicate Check**: Compares with posted history
4. **Posting**: Posts new content to channel
5. **Recording**: Saves to database to prevent duplicates
6. **Repeat**: Waits for next interval

### Post Limits

To avoid flooding:
- Maximum 3 posts per run
- 2-second delay between posts
- Only posts new (non-duplicate) content

### Stopping Auto-Posting

```
/stop_autopost
```

This pauses auto-posting but keeps configuration. Use `/start_autopost` to resume.

---

## Monitoring

### Real-Time Status

Check bot status anytime:
```
/status
```

Output example:
```
📊 Bot Status

Configuration:
• Channel: @mychannel
• Timer: 5 minutes
• Auto-posting: ✅ Active

Statistics:
• Total posts: 42
• Last post: 2024-01-15 10:30:00
• Cache entries: 15

System:
• Database: ✅ Connected
• Scraper: ✅ Ready
```

### Detailed Statistics

View comprehensive stats:
```
/stats
```

Output example:
```
📈 Detailed Statistics

Posts:
• Total: 42
• Today: 8
• Unique content: 42

Cache:
• Entries: 15
• Hit rate: 75.3%

Database:
• Size: 0.45 MB
```

### Post History

View recent posts:
```
/posted
```

Output shows last 10 posts with:
- Title
- Posted timestamp
- URL (stored, not shown)

### Logs (Deployment Platform)

**Heroku:**
```bash
heroku logs --tail
```

**Vercel:**
```bash
vercel logs
```

Look for:
- `Posted: [Title]` - Successful posts
- `Skipping duplicate: [Title]` - Duplicate prevention
- `Error:` - Issues to investigate

---

## Advanced Usage

### Multiple Admins

Configure multiple admin IDs in `.env`:

```env
ADMIN_IDS=123456789,987654321,555666777
```

All admins have full control over the bot.

### Custom Domain

If HDhub4u changes domain, update in `.env`:

```env
HDHUB4U_DOMAIN=https://new-domain.com
```

### Database Management

Database file: `bot_data.db`

**View size:**
```
/stats
```

**Backup:**
```bash
# On server
cp bot_data.db bot_data_backup.db
```

**Reset (careful!):**
```bash
# Stop bot first
rm bot_data.db
# Restart bot - new database will be created
```

### Cache Management

Cache is automatic, but you can understand it:

**Cache entries:**
- `latest_content` - Scraped content (5 min TTL)
- `links_[url]` - Download links (1 hour TTL)

**Cache stats:**
```
/stats
```

Shows hit rate - higher is better (less scraping).

### Rate Limiting

Built-in rate limiting:
- 2 seconds between posts
- Max 3 posts per cycle
- Content cached for 5 minutes
- Links cached for 1 hour

This prevents:
- Channel flooding
- Server overload
- IP blocking
- API rate limits

---

## Best Practices

### For Testing

1. Start with longer timer (10-15 min)
2. Use test channel first
3. Monitor with `/status` frequently
4. Check logs for errors
5. Verify posts in channel

### For Production

1. Use 5-10 minute timer
2. Monitor daily with `/stats`
3. Check `/posted` for accuracy
4. Keep bot as admin in channel
5. Monitor Heroku dyno hours (free tier)

### Channel Management

1. Bot must be admin
2. Give "Post Messages" permission
3. Keep bot's admin status
4. Don't remove bot from channel
5. Use channel username or ID

### Maintenance

**Daily:**
- Quick `/status` check

**Weekly:**
- Review `/stats` for trends
- Check `/posted` history
- Monitor platform (Heroku/Vercel)

**Monthly:**
- Review logs for errors
- Check database size
- Verify channel access
- Update dependencies (if needed)

### Error Recovery

**Bot stopped posting:**
1. Check `/status` - is auto-post enabled?
2. Verify channel settings
3. Check bot is still admin
4. Try `/force_post` to test
5. Restart if needed

**Duplicate posts:**
- Should never happen (database prevents)
- If it does, check database integrity
- May indicate database reset

**No content:**
- Check logs for scraping errors
- Verify HDhub4u domain is accessible
- Try manual `/force_post`

---

## FAQ

### General

**Q: Who can use this bot?**  
A: Only admins configured in ADMIN_IDS. Others get "Access denied" message.

**Q: Can I have multiple channels?**  
A: Currently supports one channel. Fork code for multi-channel support.

**Q: How do I change admin IDs?**  
A: Update ADMIN_IDS environment variable and restart bot.

### Configuration

**Q: What's the minimum timer?**  
A: 1 minute, but 5+ minutes recommended to avoid rate limits.

**Q: Can I post to a private channel?**  
A: Yes, use channel ID (starts with -100) instead of username.

**Q: Does bot need admin rights?**  
A: Yes, specifically "Post Messages" permission.

### Posting

**Q: Why isn't anything posting?**  
A: Check: 1) Auto-post enabled 2) Channel set 3) Bot is admin 4) Content available

**Q: Can I customize post format?**  
A: Yes, edit `format_post_message()` in bot.py.

**Q: How does duplicate prevention work?**  
A: URL-based tracking in SQLite database with indexed lookups.

**Q: What if I want to repost something?**  
A: Remove from database (advanced) or wait for manual feature addition.

### Technical

**Q: What database does it use?**  
A: SQLite (file-based, bot_data.db).

**Q: Is data persistent?**  
A: Yes, on Heroku with persistent dyno. Free tier may reset.

**Q: How much does it cost?**  
A: Heroku free tier has limits. Hobby tier ($7/mo) for 24/7.

**Q: Can I use PostgreSQL?**  
A: Not currently, but can be adapted.

**Q: Does it work on Vercel?**  
A: Partially - webhook mode needed for full functionality.

### Troubleshooting

**Q: Bot responds "Access denied"**  
A: Your user ID not in ADMIN_IDS. Check ID with @userinfobot.

**Q: "Channel not found" error**  
A: Verify channel name/ID and bot admin status.

**Q: Posts appear but no content**  
A: Check scraper logs. Website might be down.

**Q: Database errors**  
A: Check disk space and write permissions.

**Q: High memory usage**  
A: Normal. Restart if needed. Consider larger dyno.

---

## Quick Reference

### Daily Workflow

```
/status          # Check bot status
/stats           # View statistics  
/posted          # See recent posts
```

### Setup Commands

```
/start           # Initialize
/setchannel @ch  # Set channel
/settimer 5      # Set interval
/start_autopost  # Begin posting
```

### Control Commands

```
/stop_autopost   # Pause
/start_autopost  # Resume
/force_post      # Post now
```

---

## Support

For issues:
1. Check `/status` and logs
2. Review [DEPLOYMENT.md](DEPLOYMENT.md)
3. Read [README.md](README.md)
4. Check bot is admin in channel
5. Verify environment variables

---

## Examples

### Example 1: Initial Setup

```
User: /start
Bot: [Welcome message with status]

User: /setchannel @moviechannel
Bot: ✅ Channel set to: @moviechannel

User: /settimer 5
Bot: ✅ Auto-post interval set to: 5 minutes

User: /start_autopost
Bot: ✅ Auto-posting started!
     Posts will be published every 5 minutes.
```

### Example 2: Monitoring

```
User: /status
Bot: [Shows configuration and statistics]

User: /stats
Bot: [Shows detailed analytics]

User: /posted
Bot: [Lists recent 10 posts]
```

### Example 3: Manual Control

```
User: /force_post
Bot: 🔄 Fetching content...
     ✅ Content posted successfully!

User: /stop_autopost
Bot: ⏸️ Auto-posting stopped!

User: /start_autopost
Bot: ✅ Auto-posting started!
```

---

Happy posting! 🎬🤖

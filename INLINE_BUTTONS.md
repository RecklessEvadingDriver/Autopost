# Inline Download Buttons - Feature Guide

## Overview

The bot posts content with **inline keyboard buttons** that provide direct download links. Each button is beautifully formatted with quality indicators and server information.

## Button Layout

When content is posted to your channel, it appears like this:

```
┌─────────────────────────────────────┐
│  [Movie Poster Image]               │
│                                     │
│  🎬 Movie Title (2024)              │
│                                     │
│  📊 Quality: 1080p FHD              │
│  📅 Year: 2024                      │
│  ⭐ Rating: 8.5                     │
│  🎭 Genre: Action, Thriller         │
│                                     │
│  📝 Description text...             │
│                                     │
│  💾 5 Download Links Available      │
│  👇 Click the buttons below         │
├─────────────────────────────────────┤
│  [🎥 4K UHD]                        │  ← Button 1 (2160p)
│  [📺 1080p FHD]                     │  ← Button 2 (1080p)
│  [📺 1080p FHD]                     │  ← Button 3 (1080p Alt)
│  [📱 720p HD]                       │  ← Button 4 (720p)
│  [📱 480p SD]                       │  ← Button 5 (480p)
│  [ℹ️ More Info]                     │  ← Button 6 (Info page)
└─────────────────────────────────────┘
```

## Button Features

### 1. Quality-Based Icons

Each button has an emoji icon indicating quality:

- 🎥 **4K UHD / 2160p** - Premium ultra HD quality
- 📺 **1080p FHD** - Full HD quality (most common)
- 📱 **720p HD** - HD quality (mobile-friendly)
- 📱 **480p SD** - Standard definition (smaller file)
- 📥 **Download** - Generic download (quality unknown)

### 2. Automatic Sorting

Buttons are sorted by quality:
1. Highest quality first (4K)
2. 1080p
3. 720p
4. 480p
5. Generic downloads last

### 3. Multiple Servers

Supports various download servers:

- **HubDrive** - Primary HDhub4u server
- **HubCloud** - Alternative HDhub4u server
- **HubStream** - Streaming + download
- **PixelDrain** - Direct download
- **Mega.nz** - Cloud storage
- **Google Drive** - Google cloud
- **MediaFire** - File hosting

### 4. Smart Detection

The bot automatically:
- Detects quality from link text
- Removes duplicate links
- Filters invalid links
- Organizes by quality
- Limits to 8 buttons for clean UI

## Technical Implementation

### Quality Detection Algorithm

```python
# Pattern matching for quality
if '2160' or '4K' or 'UHD' → "4K"
elif '1080' or 'FHD' → "1080p"
elif '720' or 'HD' → "720p"
elif '480' or 'SD' → "480p"
else → "Download"
```

### Server Detection

```python
# URL-based server detection
if 'hubdrive' in url → HubDrive
elif 'hubcloud' in url → HubCloud
elif 'pixeldrain' in url → PixelDrain
# ... etc
```

### Button Generation

```python
# Each link becomes an inline button
InlineKeyboardButton(
    text="🎥 4K UHD",    # Display text with emoji
    url="https://..."    # Download link
)
```

## Example Posts

### Example 1: Movie with Multiple Qualities

```
🎬 Avengers: Endgame (2019)

📊 Quality: 1080p FHD
📅 Year: 2019
⭐ Rating: 8.4
🎭 Genre: Action, Adventure, Sci-Fi

📝 After the devastating events of Avengers: 
Infinity War, the universe is in ruins...

💾 6 Download Links Available
👇 Click the buttons below to download

[🎥 4K UHD]
[📺 1080p FHD]
[📺 1080p FHD] (Alt Server)
[📱 720p HD]
[📱 480p SD]
[ℹ️ More Info]
```

### Example 2: TV Series Episode

```
🎬 Breaking Bad S05E16 (2013)

📊 Quality: 1080p FHD
⭐ Rating: 9.9
🎭 Genre: Crime, Drama

📝 Series finale. Walter's world crumbles 
as the truth comes out...

💾 4 Download Links Available
👇 Click the buttons below to download

[📺 1080p FHD]
[📱 720p HD]
[📱 480p SD]
[ℹ️ More Info]
```

### Example 3: New Release

```
🎬 The Batman (2024)

📊 Quality: CAM
📅 Year: 2024
🎭 Genre: Action, Crime, Mystery

📝 In his second year of fighting crime, 
Batman uncovers corruption...

💾 2 Download Links Available
👇 Click the buttons below to download

[📱 720p HD]
[📥 Download]
[ℹ️ More Info]
```

## User Experience

### For Channel Viewers:

1. **Visual Appeal**: Clean, organized button layout
2. **One-Click Access**: Direct download link access
3. **Quality Choice**: Multiple quality options available
4. **Mobile-Friendly**: Works perfectly on mobile apps
5. **No Confusion**: Clear quality labels on each button

### For Admins:

1. **Automatic**: No manual button creation needed
2. **Smart**: Auto-detects quality and servers
3. **Reliable**: Duplicate filtering built-in
4. **Scalable**: Handles 1-8 links per post
5. **Flexible**: Supports multiple server types

## Configuration

### Maximum Buttons

Default: Up to 8 download buttons per post

Why 8?
- Telegram supports many buttons
- 8 provides good variety without clutter
- Keeps UI clean and readable
- Prevents overwhelming users

### Button Text Format

```
[Emoji] [Quality] [Optional: Server]

Examples:
🎥 4K UHD
📺 1080p FHD
📱 720p HD
📥 Download
ℹ️ More Info
```

### Customization

To customize buttons, edit `create_download_keyboard()` in `bot.py`:

```python
def create_download_keyboard(item: dict):
    # Modify quality_map for different emojis
    quality_map = {
        '4K': '🎥 4K UHD',      # ← Change emoji/text here
        '1080p': '📺 1080p FHD',
        # ... etc
    }
```

## Best Practices

### For Optimal Button Display:

1. **Keep titles concise** - Shorter titles = better layout
2. **Use quality detection** - Let bot auto-detect quality
3. **Test with force_post** - Verify button appearance
4. **Monitor link quality** - Ensure links are working
5. **Check mobile view** - Test on Telegram mobile app

### Troubleshooting:

**Buttons not showing?**
- Check if download links were found
- Verify links are from supported servers
- Check logs: `heroku logs --tail`

**Wrong quality labels?**
- Links may not have quality info in text
- Bot falls back to "Download" label
- Can be customized in scraper.py

**Too many/few buttons?**
- Adjust limit in `create_download_keyboard()`
- Default is 8, can be changed

## Advanced Features

### Link Validation

Bot only includes links from trusted servers:
- hdstream4u, hubstream, hubdrive, hubcloud
- pixeldrain, hblinks, buzzserver
- mega.nz, mediafire, drive.google

### Duplicate Prevention

- Tracks URLs already processed
- Filters duplicate links from same page
- Keeps only unique download options

### Sort Priority

1. 4K / 2160p (highest priority)
2. 1440p / QHD
3. 1080p / FHD
4. 720p / HD
5. 480p / SD
6. Generic downloads (lowest priority)

## Future Enhancements

Potential improvements:

- [ ] Two-column button layout for more options
- [ ] Add file size to button labels
- [ ] Server-specific emoji indicators
- [ ] Direct streaming button support
- [ ] Custom button text templates
- [ ] Button analytics tracking

---

## Support

For button-related issues:

1. Check example posts with `/force_post`
2. Verify download links are accessible
3. Review bot logs for errors
4. Ensure bot has proper channel permissions

---

Made with ❤️ for the best user experience!

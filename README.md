# HDhub4u Telegram Auto-Post Bot

An advanced Telegram bot that automatically posts HDhub4u content to your channel with admin controls, caching, and duplicate prevention.

## 🌟 Features

- ✅ **Auto-posting**: Automatically posts content every 5 minutes (configurable)
- ✅ **Admin Only**: Restricted access to authorized admins only
- ✅ **Duplicate Prevention**: Never posts the same content twice
- ✅ **Download Link Updates**: Monitors and updates download links when changed
- ✅ **Post History**: Complete record of all posted content
- ✅ **Smart Caching**: Fast performance with intelligent caching system
- ✅ **Flexible Timer**: Configure posting interval (1-60+ minutes)
- ✅ **Multiple Admin Support**: Add multiple admins
- ✅ **Statistics Dashboard**: Track posts, cache performance, and more
- ✅ **Quality Detection**: Automatically detects video quality (4K, 1080p, 720p, etc.)

## 📋 Requirements

- Python 3.11+
- Telegram Bot Token
- Admin User ID(s)
- Telegram Channel (where bot will post)

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/RecklessEvadingDriver/Autopost.git
cd Autopost
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```env
BOT_TOKEN=your_bot_token_from_botfather
ADMIN_IDS=your_telegram_user_id
```

### 4. Run the Bot

```bash
python bot.py
```

## 🔧 Configuration

### Get Bot Token

1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow instructions
3. Copy the token provided

### Get Your User ID

1. Message [@userinfobot](https://t.me/userinfobot) on Telegram
2. It will reply with your user ID
3. Use this ID in `ADMIN_IDS`

### Setup Channel

1. Create a Telegram channel
2. Add your bot as administrator
3. Give it permission to post messages
4. Use `/setchannel @yourchannel` or `/setchannel -1001234567890`

## 📱 Bot Commands

### Admin Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Initialize bot and view help | `/start` |
| `/setchannel` | Set target channel for posting | `/setchannel @mychannel` |
| `/settimer` | Set auto-post interval (minutes) | `/settimer 10` |
| `/start_autopost` | Start automatic posting | `/start_autopost` |
| `/stop_autopost` | Stop automatic posting | `/stop_autopost` |
| `/force_post` | Manually trigger a post | `/force_post` |
| `/status` | View bot status and configuration | `/status` |
| `/posted` | View recent post history | `/posted` |
| `/stats` | View detailed statistics | `/stats` |

## 🏗️ Project Structure

```
Autopost/
├── bot.py              # Main bot application
├── database.py         # Database management (SQLite)
├── scraper.py          # HDhub4u content scraper
├── cache_manager.py    # Caching system
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── Procfile           # Heroku deployment config
├── runtime.txt        # Python version for Heroku
├── vercel.json        # Vercel deployment config
├── DEPLOYMENT.md      # Detailed deployment guide
└── README.md          # This file
```

## 🎯 How It Works

1. **Scraping**: Bot scrapes latest content from HDhub4u website
2. **Caching**: Content is cached to reduce server load and improve speed
3. **Duplicate Check**: Before posting, checks if content was already posted
4. **Formatting**: Creates beautiful message with poster, title, quality, etc.
5. **Posting**: Posts to configured channel with download buttons
6. **Recording**: Saves post record to prevent duplicates
7. **Scheduling**: Repeats at configured interval (default: 5 minutes)

## 💾 Database

The bot uses SQLite for data persistence:

- **Settings**: Stores channel, timer, and configuration
- **Posts**: Records all posted content with timestamps
- **Indexed**: Fast duplicate checking and history queries

Database file: `bot_data.db` (auto-created)

## ⚡ Caching System

Smart caching improves performance:

- **Content Cache**: Latest scraped content (5 min TTL)
- **Link Cache**: Download links (1 hour TTL)
- **Statistics**: Real-time cache hit/miss tracking
- **Auto-cleanup**: Expired entries are automatically removed

## 📊 Features in Detail

### Auto-Posting
- Configurable interval (1+ minutes)
- Automatic retry on failures
- Rate limiting to avoid flooding
- Pause/resume capability

### Duplicate Prevention
- URL-based duplicate detection
- Fast indexed database lookups
- Permanent history storage
- No false positives

### Download Links
- Extracts multiple download links
- Inline keyboard buttons
- Quality labels (1080p, 720p, etc.)
- Link update monitoring

### Admin Controls
- Multi-admin support
- Secure authentication
- Command-based configuration
- Real-time status updates

## 🌐 Deployment

Detailed deployment guides available for:

- **Heroku** (Recommended for 24/7 operation)
- **Vercel** (Serverless option)

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete instructions.

### Quick Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

```bash
# Via CLI
heroku create your-app-name
heroku config:set BOT_TOKEN="your_token"
heroku config:set ADMIN_IDS="your_id"
git push heroku main
```

## 🔍 Monitoring

### View Status
```
/status
```
Shows:
- Current configuration
- Post count
- Last post time
- Cache statistics

### View Statistics
```
/stats
```
Shows:
- Total posts
- Today's posts
- Cache hit rate
- Database size

### View History
```
/posted
```
Shows recent 10 posts

## 🛠️ Troubleshooting

### Bot Not Posting

1. Check bot is running: `/status`
2. Verify channel is set: `/setchannel @yourchannel`
3. Ensure auto-post is enabled: `/start_autopost`
4. Check bot is admin in channel
5. View logs for errors

### Permission Errors

- Bot must be admin in channel
- Bot needs "Post Messages" permission
- Channel username must be correct

### Database Issues

- Database auto-creates on first run
- Check write permissions
- Ensure sufficient disk space

## 🔐 Security

- Admin-only access (non-admins blocked)
- Environment variables for sensitive data
- No hardcoded credentials
- Secure token handling

## 📝 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Telegram Bot API Token | Yes |
| `ADMIN_IDS` | Comma-separated admin user IDs | Yes |
| `HDHUB4U_DOMAIN` | Custom HDhub4u domain | No |

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This bot is for educational purposes. Ensure you have rights to post content and comply with Telegram's Terms of Service and local laws.

## 📞 Support

For issues or questions:

1. Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment help
2. Review bot logs for errors
3. Verify configuration with `/status`
4. Open an issue on GitHub

## 🎉 Credits

Based on HDhub4u CloudStream3 provider logic. Adapted for Telegram bot use.

## 🚀 Future Features

- [ ] Multiple channel support
- [ ] Content filtering by genre
- [ ] Custom message templates
- [ ] Webhook mode for Vercel
- [ ] Redis cache option
- [ ] PostgreSQL support
- [ ] Web dashboard
- [ ] Backup/restore functionality

---

Made with ❤️ for the community

**Star ⭐ this repo if you find it useful!**

# HDhub4u Telegram Auto-Post Bot - Deployment Guide

This guide covers deployment on both Heroku and Vercel platforms.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Heroku Deployment](#heroku-deployment)
- [Vercel Deployment](#vercel-deployment)
- [Environment Variables](#environment-variables)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before deploying, you need:

1. **Telegram Bot Token**
   - Message [@BotFather](https://t.me/BotFather) on Telegram
   - Send `/newbot` and follow instructions
   - Copy the token provided

2. **Admin User IDs**
   - Message [@userinfobot](https://t.me/userinfobot) on Telegram
   - Send any message to get your user ID
   - Note down your ID (and any other admin IDs)

3. **A Telegram Channel**
   - Create a channel where content will be posted
   - Add your bot as an administrator with posting permissions
   - Get the channel username (e.g., `@mychannel`) or ID

---

## Heroku Deployment

Heroku is recommended for 24/7 operation with scheduled auto-posting.

### Step 1: Create Heroku Account
1. Sign up at [heroku.com](https://heroku.com)
2. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### Step 2: Deploy to Heroku

#### Option A: Via Heroku CLI

```bash
# Login to Heroku
heroku login

# Navigate to project directory
cd /path/to/Autopost

# Create new Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set BOT_TOKEN="your_bot_token_here"
heroku config:set ADMIN_IDS="123456789,987654321"

# Deploy
git push heroku main

# Scale the worker
heroku ps:scale web=1

# View logs
heroku logs --tail
```

#### Option B: Via Heroku Dashboard

1. Go to [Heroku Dashboard](https://dashboard.heroku.com)
2. Click "New" → "Create new app"
3. Choose app name and region
4. Under "Deploy" tab:
   - Connect to GitHub
   - Search for "Autopost" repository
   - Enable automatic deploys (optional)
5. Under "Settings" tab:
   - Click "Reveal Config Vars"
   - Add `BOT_TOKEN` and `ADMIN_IDS`
6. Under "Resources" tab:
   - Ensure "web" dyno is enabled

### Step 3: Verify Deployment

```bash
# Check if app is running
heroku ps

# View logs
heroku logs --tail

# Open app URL
heroku open
```

### Heroku Features:
- ✅ 24/7 operation
- ✅ Automatic restarts
- ✅ Built-in logging
- ✅ Easy scaling
- ✅ Free tier available (with limitations)

---

## Vercel Deployment

**Note**: Vercel is serverless and better suited for webhook-based bots. For scheduled auto-posting, Heroku is recommended. However, you can use Vercel with external cron services.

### Step 1: Prepare for Vercel

Modify `bot.py` to support webhook mode (optional for Vercel):

```python
# For Vercel, you'll need webhook mode
# Add this to bot.py if using Vercel
```

### Step 2: Deploy to Vercel

#### Option A: Via Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Set environment variables
vercel env add BOT_TOKEN
vercel env add ADMIN_IDS

# Deploy to production
vercel --prod
```

#### Option B: Via Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import from GitHub
4. Select "Autopost" repository
5. Configure:
   - Framework Preset: Other
   - Root Directory: ./
6. Add Environment Variables:
   - `BOT_TOKEN`: Your bot token
   - `ADMIN_IDS`: Your admin IDs (comma-separated)
7. Click "Deploy"

### Step 3: Configure Webhook (for Vercel)

```bash
# Set webhook URL
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://your-app.vercel.app/webhook"
```

### Vercel Limitations:
- ⚠️ Serverless (not always running)
- ⚠️ Execution time limits
- ⚠️ Better for webhook mode, not polling
- ⚠️ May need external cron for scheduled tasks

**Recommendation**: Use Heroku for this bot due to auto-posting requirements.

---

## Environment Variables

Both platforms require these environment variables:

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `BOT_TOKEN` | Telegram Bot API Token from @BotFather | `123456:ABC-DEF...` | Yes |
| `ADMIN_IDS` | Comma-separated admin user IDs | `123456789,987654321` | Yes |
| `HDHUB4U_DOMAIN` | Custom HDhub4u domain (optional) | `https://hdhub4u.rehab` | No |

### Setting Environment Variables:

**Heroku:**
```bash
heroku config:set VARIABLE_NAME="value"
```

**Vercel:**
```bash
vercel env add VARIABLE_NAME
```

---

## Post-Deployment Setup

Once deployed, interact with your bot:

1. **Start the bot**
   ```
   /start
   ```

2. **Set the channel**
   ```
   /setchannel @yourchannel
   ```

3. **Set posting interval** (default: 5 minutes)
   ```
   /settimer 5
   ```

4. **Start auto-posting**
   ```
   /start_autopost
   ```

5. **Check status**
   ```
   /status
   ```

---

## Troubleshooting

### Common Issues:

**1. Bot not responding**
- Check if bot is running: `heroku logs --tail`
- Verify BOT_TOKEN is correct
- Ensure bot is started with `/start`

**2. Cannot post to channel**
- Make sure bot is added as admin in the channel
- Verify channel username/ID is correct
- Check bot has permission to post

**3. App sleeping on Heroku (Free tier)**
- Heroku free tier sleeps after 30 minutes of inactivity
- Upgrade to Hobby tier for 24/7 operation
- Or use a service like UptimeRobot to ping your app

**4. Database errors**
- Database file is created automatically
- For persistence on Heroku, consider using PostgreSQL addon

**5. Memory issues**
- Monitor memory usage: `heroku logs --tail`
- Clear old posts: The bot has automatic cleanup
- Consider upgrading Heroku dyno

### Logs:

**Heroku:**
```bash
heroku logs --tail -a your-app-name
```

**Vercel:**
```bash
vercel logs
```

### Restart Bot:

**Heroku:**
```bash
heroku restart
```

**Vercel:**
- Redeploy automatically restarts

---

## Maintenance

### Update Bot Code:

**Heroku:**
```bash
git pull origin main
git push heroku main
```

**Vercel:**
- Push to GitHub (auto-deploys if enabled)
- Or run `vercel --prod`

### Monitor Performance:

```bash
# View bot status
/status

# View statistics
/stats

# View recent posts
/posted
```

### Clear Old Data:

The database automatically manages old posts, but you can:
- Monitor database size via `/stats`
- Old posts are kept for history
- Consider manual cleanup after 90+ days if needed

---

## Support

For issues:
1. Check logs first
2. Verify environment variables
3. Ensure all dependencies are installed
4. Check bot permissions in channel

---

## Cost Estimates

### Heroku:
- Free tier: Limited hours per month (sleeps after inactivity)
- Hobby tier: $7/month (24/7 operation, no sleeping)
- Standard tier: $25+/month (better performance)

### Vercel:
- Free tier: Generous limits for hobby projects
- Pro tier: $20/month (better limits)

**Recommendation**: Start with Heroku Free tier for testing, upgrade to Hobby for production 24/7 operation.

---

## Security Notes

- Never commit `.env` file to git
- Keep BOT_TOKEN secret
- Only share admin access with trusted users
- Regularly rotate bot token if compromised
- Use environment variables for all sensitive data

---

## Next Steps

After successful deployment:
1. Test with `/force_post` command
2. Monitor first few auto-posts
3. Adjust timer as needed with `/settimer`
4. Check `/stats` regularly
5. Review `/posted` history

Enjoy your automated posting bot! 🤖

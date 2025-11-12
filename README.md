# Sprite Sheet Cropper

A free, browser-based tool for cropping and processing sprite sheets.

## Features

- 🎯 Auto-detect frame layouts
- 📐 Visual grid lines to separate frames
- ✂️ Crop margins for each frame
- 📥 Download processed sprite sheets
- 🌐 Works entirely in your browser (no server needed)

## Free Hosting Options

### Option 1: GitHub Pages (Recommended)

1. **Create a GitHub account** (if you don't have one): https://github.com
2. **Create a new repository**:
   - Click "New repository"
   - Name it (e.g., `sprite-sheet-cropper`)
   - Make it **Public**
   - Click "Create repository"
3. **Upload files**:
   - Click "uploading an existing file"
   - Drag and drop `index.html` (or rename `sprite_sheet_tool.html` to `index.html`)
   - Click "Commit changes"
4. **Enable GitHub Pages**:
   - Go to Settings → Pages
   - Under "Source", select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Click "Save"
5. **Your site will be live at**: `https://yourusername.github.io/repository-name`

### Option 2: Netlify Drop (Easiest - No Account Needed!)

1. Go to: https://app.netlify.com/drop
2. Drag and drop your folder containing `index.html`
3. Get instant URL - that's it!

### Option 3: Vercel

1. Go to: https://vercel.com
2. Sign up (free)
3. Click "Add New Project"
4. Drag and drop your folder or connect GitHub
5. Deploy instantly

### Option 4: Surge.sh (Command Line)

```bash
# Install Surge (requires Node.js)
npm install -g surge

# Navigate to your folder
cd "Sprite Edit"

# Deploy
surge

# Follow prompts - you'll get a free URL like: yourname.surge.sh
```

## Quick Start

1. Open `index.html` in any modern web browser
2. Select a sprite sheet image
3. Click "Auto Detect Frames" or manually set columns/rows
4. Adjust crop margins if needed
5. Click "Process Sprite Sheet"
6. Download your cropped sprite sheet!

## Browser Support

Works in all modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

## License

Free to use for any purpose.


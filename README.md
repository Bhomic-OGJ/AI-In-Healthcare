# Brochure Showcase Website

A beautiful, modern HTML website to showcase your brochure with interactive features and responsive design.

## Features

### 🎨 **Modern Design**
- Clean, professional interface with gradient backgrounds
- Smooth animations and transitions
- Mobile-responsive layout
- Custom scrollbar styling

### 📖 **Interactive Page Viewer**
- Page-by-page navigation with previous/next buttons
- Thumbnail navigation for quick page access
- Full-screen modal view for detailed inspection
- Keyboard navigation (arrow keys)
- Touch/swipe support for mobile devices
- Zoom controls (zoom in/out/reset)

### 📱 **Responsive Design**
- Works perfectly on desktop, tablet, and mobile
- Mobile-optimized navigation menu
- Touch-friendly controls
- Adaptive layout for all screen sizes

### 🔗 **Working Links & Features**
- Download PDF functionality
- Contact form with validation
- Social media sharing
- Direct page linking via URL hash
- Print individual pages
- Copy link functionality

### ⚡ **Performance**
- Lazy loading for images
- Optimized animations
- Smooth scrolling
- Intersection Observer for efficient animations

## Setup Instructions

### 1. **Add Your Assets**
Place your brochure files in the `assets/` folder:

```
assets/
├── brochure.pdf          # Your main PDF brochure
├── cover.jpg            # Cover image (400x600px recommended)
├── page1.jpg            # Page 1 image
├── page2.jpg            # Page 2 image
├── page3.jpg            # Page 3 image
├── ...                  # Continue for all pages
└── page8.jpg            # Last page image
```

### 2. **Configure Page Count**
Update the `totalPages` variable in `script.js` if you have a different number of pages:

```javascript
const totalPages = 8; // Change this to your actual page count
```

### 3. **Customize Content**
Edit the following in `index.html`:
- Company name and branding
- Contact information
- Social media links
- Section content

### 4. **Update Colors (Optional)**
Modify the CSS variables in `styles.css`:

```css
:root {
    --primary-color: #2563eb;     /* Main brand color */
    --accent-color: #f59e0b;      /* Accent color */
    /* ... other colors */
}
```

## Usage

### **Viewing Pages**
- Use arrow buttons or keyboard arrows to navigate
- Click thumbnails for quick page access
- Click on any page image for full-screen view
- Use zoom controls for detailed inspection

### **Mobile Navigation**
- Swipe left/right on pages to navigate
- Tap thumbnails to jump to specific pages
- Use the hamburger menu for navigation

### **Sharing & Downloading**
- Click "Download PDF" to get the full brochure
- Use the share functionality to copy links
- Direct page links work with URL hash (e.g., `#page-3`)

### **Contact Form**
- Fill out the contact form for inquiries
- Form includes validation and success notifications

## Browser Support

- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Mobile browsers

## Features Breakdown

### **Hero Section**
- Eye-catching gradient background
- 3D brochure preview with hover effects
- Call-to-action buttons for immediate engagement

### **Page Viewer**
- Professional page display with numbered overlays
- Smooth transitions between pages
- Thumbnail strip for visual navigation
- Full-screen modal capability

### **Features Grid**
- Highlight key benefits
- Icon-based visual representation
- Hover animations for interactivity

### **Download Section**
- Clear download call-to-action
- File information display
- Visual PDF preview

### **Contact Section**
- Multiple contact methods
- Functional contact form
- Professional layout

## Customization Tips

### **Adding More Pages**
1. Add new page images to the `assets/` folder
2. Update `totalPages` in `script.js`
3. The system will automatically generate thumbnails and grid items

### **Changing Images**
- Replace placeholder images with your actual brochure pages
- Recommended sizes:
  - Cover: 400x600px
  - Pages: 800x1000px (for viewer)
  - Thumbnails: 100x140px (auto-generated)

### **Modifying Layout**
- All sections use semantic HTML5 structure
- CSS Grid and Flexbox for responsive layouts
- Easy to modify spacing and sizing

## Technical Details

### **Technologies Used**
- HTML5 semantic markup
- CSS3 with custom properties
- Vanilla JavaScript (no dependencies)
- Font Awesome icons
- Google Fonts (Inter)

### **Performance Features**
- Lazy loading for images
- Efficient event handling
- Optimized animations with CSS transforms
- Intersection Observer for scroll animations

### **Accessibility**
- Semantic HTML structure
- ARIA labels where appropriate
- Keyboard navigation support
- High contrast colors
- Focus states for interactive elements

## Troubleshooting

### **Images Not Loading**
- Check file paths in the `assets/` folder
- Ensure image formats are supported (JPG, PNG)
- Verify file names match the expected pattern (`page1.jpg`, `page2.jpg`, etc.)

### **PDF Download Not Working**
- Ensure `brochure.pdf` exists in the `assets/` folder
- Check file permissions
- Verify the file path in `script.js`

### **Mobile Issues**
- Ensure viewport meta tag is present
- Check touch event handling
- Test on actual mobile devices

## License

This project is open source and available under the MIT License.

---

**Need Help?**
If you encounter any issues or need assistance with customization, feel free to reach out through the contact form or check the documentation.

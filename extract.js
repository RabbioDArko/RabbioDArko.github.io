const fs = require('fs');
const path = require('path');

try {
    const html = fs.readFileSync(path.join(__dirname, 'Files/Clash of Beast - My Framer Site.htm'), 'utf8');
    
    // Remove scripts and styles
    let text = html.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '');
    text = text.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '');
    
    // Remove SVG and path tags as they often contain huge data
    text = text.replace(/<svg[^>]*>[\s\S]*?<\/svg>/gi, '');
    
    // Replace all other tags with newline
    text = text.replace(/<[^>]+>/g, '\n');
    
    // Clean up whitespace
    text = text.replace(/&nbsp;/gi, ' ');
    text = text.replace(/\n\s*\n/g, '\n');
    
    console.log(text.substring(0, 5000));
} catch(e) {
    console.error(e);
}

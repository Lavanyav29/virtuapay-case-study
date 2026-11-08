import os

svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M16.19 2H7.81C4.6 2 2 4.6 2 7.81V16.19C2 19.4 4.6 22 7.81 22H16.19C19.4 22 22 19.4 22 16.19V7.81C22 4.6 19.4 2 16.19 2ZM11.16 16.48H8.5V7.52H12.78C13.91 7.52 14.83 8.44 14.83 9.57C14.83 10.15 14.59 10.67 14.21 11.04C14.8 11.41 15.19 12.06 15.19 12.8C15.19 14.1 14.13 15.16 12.83 15.16H11.16V16.48ZM11.16 11.39H12.78C13.2 11.39 13.54 11.05 13.54 10.63C13.54 10.21 13.2 9.87 12.78 9.87H11.16V11.39ZM11.16 14.84H12.83C13.43 14.84 13.92 14.35 13.92 13.75C13.92 13.15 13.43 12.66 12.83 12.66H11.16V14.84Z" fill="currentColor"/></svg>'

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace('<i class="ph-bold ph-rss"></i>', svg)
        new_content = new_content.replace('<i class="ph ph-rss"></i>', svg)
        
        # Also ensure header links have d-flex for alignment if they contain the SVG
        # This is a bit risky but let's try to be specific
        header_pattern = 'class="tw-text-xl text-dark-600">' + svg
        header_replacement = 'class="tw-text-xl text-dark-600 d-flex align-items-center">' + svg
        new_content = new_content.replace(header_pattern, header_replacement)

        if content != new_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")

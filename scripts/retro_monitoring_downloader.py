#!/usr/bin/env python3
"""
90s Network Monitoring References Downloader
Downloads web pages and content from vintage monitoring tools research

Usage: python download_references.py
"""

import requests
import os
import time
import urllib.parse
from pathlib import Path
from datetime import datetime
import json

class RetroMonitoringDownloader:
    def __init__(self, output_dir="/Users/punk1290/git/retro-graph/proompts/references"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Create subdirectories for different types of content
        self.html_dir = self.output_dir / "html_pages"
        self.images_dir = self.output_dir / "images"
        self.docs_dir = self.output_dir / "documents"
        self.metadata_dir = self.output_dir / "metadata"
        
        for dir_path in [self.html_dir, self.images_dir, self.docs_dir, self.metadata_dir]:
            dir_path.mkdir(exist_ok=True)
        
        # HTTP session with retro-appropriate user agent
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',  # Retro browser
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        })
        
        # URLs found during research
        self.urls = [
            # MRTG Related
            "https://oss.oetiker.ch/mrtg/",
            "https://en.wikipedia.org/wiki/Multi_Router_Traffic_Grapher",
            "https://www.satsignal.eu/mrtg/performance_howto.php",
            "https://github.com/oetiker/mrtg",
            "https://www.softpedia.com/get/Network-Tools/Network-Monitoring/MRTG.shtml",
            
            # Big Brother / Xymon
            "https://en.wikipedia.org/wiki/Big_Brother_(software)",
            "https://xymon.sourceforge.io/",
            "https://www.linuxjournal.com/article/2225",
            "https://kin.klever.net/bigbrother/",
            
            # Cricket / RRDtool
            "http://cricket.sourceforge.net/support/FAQ/",
            "https://cricket.sourceforge.net/support/doc/reference.html",
            "https://cricket.sourceforge.net/rrd.php",
            "https://en.wikipedia.org/wiki/RRDtool",
            "https://www.networkcomputing.com/wireless-infrastructure/exploring-cricket",
            "https://www.ws.afnog.org/afnog2001/routing/82-noctools/cricket.htm",
            "https://www.drdobbs.com/beyond-mrtg/199100951",
            
            # HP OpenView
            "https://en.wikipedia.org/wiki/HP_OpenView",
            "https://www.itprotoday.com/compute-engines/what-hp-openview",
            "https://www.networkworld.com/article/2299042/hp-openview.html",
            
            # General Monitoring History
            "https://www.whatsupgold.com/blog/a-brief-history-of-network-monitoring",
            "https://live8wire.wordpress.com/network/monitoring-tools/",
            "https://www.websentra.com/best-mrtg-alternatives/",
            "https://staff.fnwi.uva.nl/j.blom/gigaport/tools/monitor_tools.html",
            
            # Technical Documentation
            "https://www.cs.rutgers.edu/~terminals/mrtg/mrtg-2.5.4c/mrtg-conf.html",
            "https://zarbi.chem.yale.edu/bb/help/bb-man.html",
            "https://www.loriotpro.com/Products/On-line_Documentation_V5/LoriotProDoc_EN/H8-Main_Process/H8-D4_MRTG_style_Graph_Process_EN.htm",
            
            # Modern context / comparisons
            "https://www.altaro.com/hyper-v/how-to-meter-track-hyper-v-networking-performance-mrtg/",
            "https://www.paessler.com/monitoring/application/mrtg-for-windows",
            "https://thwack.solarwinds.com/product-forums/network-performance-monitor-npm/f/forum/78109/1-page---all-interface-graphs-wanted-help-me-kill-mrtg",
        ]
        
        self.metadata = {
            "download_date": datetime.now().isoformat(),
            "purpose": "Research for retro 90s network monitoring tool design",
            "tools_researched": ["MRTG", "Big Brother", "Cricket", "RRDtool", "HP OpenView"],
            "downloaded_urls": []
        }

    def sanitize_filename(self, url):
        """Convert URL to safe filename"""
        # Parse URL and create meaningful filename
        parsed = urllib.parse.urlparse(url)
        domain = parsed.netloc.replace('www.', '')
        path = parsed.path.replace('/', '_').replace('.', '_')
        
        # Create filename with domain and path
        filename = f"{domain}{path}"
        if not filename.endswith('.html'):
            filename += '.html'
            
        # Remove invalid characters and limit length
        filename = "".join(c for c in filename if c.isalnum() or c in '-_.')
        return filename[:100]  # Limit filename length

    def download_page(self, url, delay=1):
        """Download a single web page with error handling"""
        try:
            print(f"Downloading: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # Save HTML content
            filename = self.sanitize_filename(url)
            filepath = self.html_dir / filename
            
            with open(filepath, 'w', encoding='utf-8', errors='ignore') as f:
                f.write(response.text)
            
            # Save metadata
            page_metadata = {
                "url": url,
                "filename": filename,
                "status_code": response.status_code,
                "content_type": response.headers.get('content-type', ''),
                "content_length": len(response.text),
                "downloaded_at": datetime.now().isoformat()
            }
            
            self.metadata["downloaded_urls"].append(page_metadata)
            print(f"✓ Saved: {filename}")
            
            # Be nice to servers
            time.sleep(delay)
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Failed to download {url}: {e}")
            return False
        except Exception as e:
            print(f"✗ Error saving {url}: {e}")
            return False

    def download_all(self):
        """Download all URLs with progress tracking"""
        print(f"Starting download of {len(self.urls)} references...")
        print(f"Output directory: {self.output_dir.absolute()}")
        print("-" * 60)
        
        successful = 0
        failed = 0
        
        for i, url in enumerate(self.urls, 1):
            print(f"[{i}/{len(self.urls)}] ", end="")
            
            if self.download_page(url):
                successful += 1
            else:
                failed += 1
        
        # Save metadata
        self.metadata.update({
            "total_urls": len(self.urls),
            "successful_downloads": successful,
            "failed_downloads": failed
        })
        
        metadata_file = self.metadata_dir / "download_metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(self.metadata, f, indent=2)
        
        print("-" * 60)
        print(f"Download complete!")
        print(f"✓ Successful: {successful}")
        print(f"✗ Failed: {failed}")
        print(f"📁 Files saved to: {self.output_dir.absolute()}")
        print(f"📋 Metadata saved to: {metadata_file}")

    def create_index(self):
        """Create an HTML index of downloaded content"""
        index_html = """<!DOCTYPE html>
<html>
<head>
    <title>90s Network Monitoring References</title>
    <style>
        body { font-family: monospace; background: #f0f0f0; margin: 20px; }
        h1 { color: #008000; }
        .category { margin: 20px 0; }
        .url-list { margin-left: 20px; }
        .url-item { margin: 5px 0; }
        a { color: #0000ff; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .status-ok { color: #008000; }
        .status-fail { color: #ff0000; }
        .retro-border { border: 2px solid #000; padding: 10px; }
    </style>
</head>
<body>
    <div class="retro-border">
        <h1>90s Network Monitoring Tool References</h1>
        <p><strong>Downloaded:</strong> """ + self.metadata["download_date"] + """</p>
        <p><strong>Purpose:</strong> """ + self.metadata["purpose"] + """</p>
        
        <h2>Downloaded Pages</h2>
"""
        
        # Group URLs by tool type
        categories = {
            "MRTG": ["mrtg", "router", "traffic", "grapher"],
            "Big Brother": ["bigbrother", "bb", "xymon"],
            "Cricket & RRDtool": ["cricket", "rrd"],
            "HP OpenView": ["openview", "hp"],
            "General": []  # catch-all
        }
        
        for category, keywords in categories.items():
            index_html += f'<div class="category"><h3>{category}</h3><div class="url-list">'
            
            for page in self.metadata["downloaded_urls"]:
                url = page["url"].lower()
                if any(keyword in url for keyword in keywords) or category == "General":
                    status_class = "status-ok" if page["status_code"] == 200 else "status-fail"
                    index_html += f'''
                    <div class="url-item">
                        <span class="{status_class}">●</span>
                        <a href="html_pages/{page['filename']}" target="_blank">{page['url']}</a>
                        <small>({page['content_length']} bytes)</small>
                    </div>'''
            
            index_html += '</div></div>'
        
        index_html += """
        <h2>Tools Researched</h2>
        <ul>
"""
        for tool in self.metadata["tools_researched"]:
            index_html += f"<li>{tool}</li>"
        
        index_html += """
        </ul>
        
        <p><em>Use these references to study the visual design patterns of 90s network monitoring tools.</em></p>
    </div>
</body>
</html>"""
        
        index_file = self.output_dir / "index.html"
        with open(index_file, 'w') as f:
            f.write(index_html)
        
        print(f"📄 Index created: {index_file}")

def main():
    """Main function to run the downloader"""
    downloader = RetroMonitoringDownloader()
    
    try:
        downloader.download_all()
        downloader.create_index()
        print("\n🎉 All done! Open 'index.html' to browse your downloaded references.")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Download interrupted by user")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")

if __name__ == "__main__":
    main()

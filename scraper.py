
import requests
from bs4 import BeautifulSoup
import schedule
import time
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def scrape_news():
    sources = [
        'https://www.bodyshopbusiness.com/',
        'https://www.fenderbender.com/',
        'https://www.repairerdrivennews.com/'
    ]
    
    articles = []
    
    for source in sources:
        try:
            response = requests.get(source)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Adjust selectors based on actual website structure
            for article in soup.find_all('article')[:5]:
                title = article.find('h2').text.strip()
                link = article.find('a')['href']
                articles.append({
                    'title': title,
                    'link': link,
                    'source': source
                })
        except Exception as e:
            print(f"Error scraping {source}: {str(e)}")
    
    return articles

def generate_newsletter(articles):
    newsletter = "<h1>Auto Collision Repair Industry News</h1>"
    newsletter += f"<p>Weekly Update for {datetime.now().strftime('%B %d, %Y')}</p><hr>"
    
    for article in articles:
        newsletter += f"""
        <div style='margin-bottom: 20px;'>
            <h3><a href='{article['link']}'>{article['title']}</a></h3>
            <p>Source: {article['source']}</p>
        </div>
        """
    
    return newsletter

def send_email(content):
    message = Mail(
        from_email='your-verified-sender@domain.com',
        to_emails=['recipient@domain.com'],
        subject=f'Auto Repair Industry News - {datetime.now().strftime("%B %d, %Y")}',
        html_content=content)
    
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f'Newsletter sent! Status code: {response.status_code}')
    except Exception as e:
        print(f'Error sending email: {str(e)}')

def job():
    articles = scrape_news()
    newsletter = generate_newsletter(articles)
    send_email(newsletter)

# Schedule the job for every Monday at 8am PT
schedule.every().monday.at('08:00').do(job)

if __name__ == "__main__":
    print("Starting news scraper...")
    while True:
        schedule.run_pending()
        time.sleep(60)

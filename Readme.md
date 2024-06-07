# BidScape - Online Auction System

 online auction system. It is a web-based platform that facilitates the buying and selling of goods and products through an auction format. It provides a virtual marketplace where individuals or businesses can bid on items, and the highest bidder wins the item being auctioned. The website also cntains tendering feature. Tenders are commonly used in public procurement processes by a company, organization, or government agency for suppliers or contractors to submit competitive bids to supply goods or products, and the lowest bidder wins the item being auctioned. The online auction system offers a convenient and efficient way for sellers to reach a large number of potential buyers and for buyers to access a wide range of products and services. It eliminates geographical limitations and allows participants from different locations to engage in bidding activities.

## Features

- A user interface for users to register.
- The seller is able to create an auction for selling a product or service with an expiry timeline.
- Sellers can select the type of bidding, either auction or tender.
- The seller can select categories for the products, such as mobiles, automobiles, real estate, electronics, etc., that will be put up for auction.
- Bidders can bid in increasing order.
- The bidder can post queries for the product on the posted auction, and the seller should be able to answer questions.
- No bids for the same amount will be accepted. 
- For auctions, when the timeline expires, the highest bidder wins the item being auctioned, and the order will be placed.
- For tenders, when the timeline expires, the lowest bidder wins the item being auctioned, and the order will be placed.
- If no bids are received even after the timeline expires, the status changes to not sold. 
- Once the timeline expires, no bids will be accepted. 
- A leaderboard to showcase the winners of the auction.

## Technologies Used

### Frontend:
- HTML
- CSS
- Bootstrap 
- JavaScript

### Backend:
- Python
- Django
- Mysql

## Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```
### Deployment

To deploy this project run:

```bash
python manage.py runserver
```
Open your browser and browse to the following address:

```bash
http://localhost:8000/
```
from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        # Create a sample user (if none exists)
        user, created = User.objects.get_or_create(username='hostuser', defaults={
            'email': 'host@example.com',
            'password': 'pbkdf2_sha256$260000$...'  # Use proper hashing or create via create_user()
        })

        # Create sample listings
        sample_listings = [
            {'title': 'Cozy Apartment', 'description': 'Nice and cozy apartment downtown', 'price_per_night': 75.0},
            {'title': 'Beach House', 'description': 'Lovely beach house with ocean views', 'price_per_night': 150.0},
            {'title': 'Mountain Cabin', 'description': 'Rustic cabin in the mountains', 'price_per_night': 90.0},
        ]

        for listing_data in sample_listings:
            listing, created = Listing.objects.get_or_create(
                title=listing_data['title'],
                defaults={
                    'description': listing_data['description'],
                    'price_per_night': listing_data['price_per_night'],
                    'host': user,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(f"Listing already exists: {listing.title}")

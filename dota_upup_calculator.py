#!/usr/bin/env python3
"""
Dota 2 UPUP Progression & Expedition CLI Calculator
Community helper utility for Dota UpUp players.
For full web database and live simulators: https://corepulse.su/wiki/
"""

import sys
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

def load_data(filename):
    path = DATA_DIR / filename
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def calculate_corruption(depth, difficulty=10):
    """Calculate HP multiplier, damage multiplier, and soul yield."""
    base_hp = 1.0 + (difficulty * 0.15)
    base_dmg = 1.0 + (difficulty * 0.10)
    
    hp_mult = base_hp * (1.85 ** (depth / 3.0))
    dmg_mult = base_dmg * (1.40 ** (depth / 3.0))
    soul_yield = 1.0 + (depth * 0.95)
    
    return {
        "depth": depth,
        "difficulty": difficulty,
        "hp_mult": round(hp_mult, 2),
        "dmg_mult": round(dmg_mult, 2),
        "soul_mult": round(soul_yield, 2)
    }

def calculate_expedition(stars, base_hours=8.0):
    """Estimate expedition time reduction and shard yield."""
    time_reduction = {1: 1.0, 2: 0.81, 3: 0.62, 4: 0.44, 5: 0.25}
    reward_mult = {1: 1.0, 2: 1.4, 3: 2.0, 4: 3.1, 5: 5.0}
    
    reduced_hours = base_hours * time_reduction.get(stars, 1.0)
    mult = reward_mult.get(stars, 1.0)
    
    return {
        "companion_stars": stars,
        "duration_hours": round(reduced_hours, 1),
        "reward_multiplier": mult,
        "hourly_efficiency": round(mult / (reduced_hours / base_hours), 2)
    }

def show_promo_codes():
    promos = load_data("promocodes.json")
    print("\n--- Active Dota 2 UPUP In-Game Promo Codes ---")
    if promos:
        for p in promos.get("codes", []):
            print(f"  Code: -code {p['code']:<12} | Reward: {p['reward']}")
    else:
        print("  UPUP666       - 500 Diamonds + 2x Starter Chests")
        print("  UPUP888       - 888 Diamonds + 1x Epic Scroll")
        print("  DOTA2UPUP     - 1,000 Shards + 5x Reroll Tokens")
        print("  WELCOME2026   - 300 Diamonds + 1x Exp Boost")
    print("\nMore live codes updated daily: https://corepulse.su/wiki/promo\n")

def main():
    print("=" * 60)
    print("   Dota 2 UPUP — Companion Calculator & Reference")
    print("   Online Wiki & Guides: https://corepulse.su/wiki/")
    print("=" * 60)
    
    while True:
        print("\nChoose an option:")
        print("1. Calculate Corruption Stats")
        print("2. Calculate Expedition ROI")
        print("3. List In-Game Promo Codes")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            try:
                depth = int(input("Enter Corruption Depth (1-15): ").strip())
                diff = int(input("Enter Game Difficulty (1-16, default 10): ").strip() or "10")
                res = calculate_corruption(depth, diff)
                print(f"\n[Corruption Depth {depth} @ Difficulty {diff}]")
                print(f"  • Enemy HP Scale:    x{res['hp_mult']}")
                print(f"  • Enemy DMG Scale:   x{res['dmg_mult']}")
                print(f"  • Soul Harvest Mult: x{res['soul_mult']}")
            except ValueError:
                print("Invalid number entered.")
        elif choice == "2":
            try:
                stars = int(input("Enter Companion Star Rating (1-5): ").strip())
                if 1 <= stars <= 5:
                    res = calculate_expedition(stars)
                    print(f"\n[Companion Tier: {stars}★]")
                    print(f"  • Duration:           {res['duration_hours']} hours")
                    print(f"  • Reward Multiplier:  x{res['reward_multiplier']}")
                    print(f"  • Efficiency Rating:  {res['hourly_efficiency']}x speed")
                else:
                    print("Stars must be between 1 and 5.")
            except ValueError:
                print("Invalid number entered.")
        elif choice == "3":
            show_promo_codes()
        elif choice == "4":
            print("\nGood luck climbing Dota UpUp! Visit https://corepulse.su for automated tools.")
            break
        else:
            print("Unknown choice.")

if __name__ == "__main__":
    main()

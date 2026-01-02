# ♠️ Blackjack Game Design (Python)

A console-based implementation of the classic **Blackjack (21)** card game, developed in Python.  
The project focuses on **game logic, rule enforcement, and clean functional design** rather than UI.

---

## 🎯 Project Objectives
- Implement Blackjack rules from scratch
- Simulate a full 52-card deck
- Handle scoring logic including **Ace flexibility (1 or 11)**
- Apply deterministic dealer behavior (hit until 17)

---

## 🧠 Game Rules Implemented
- Standard 52-card deck (no jokers)
- Face cards (J, Q, K) count as 10
- Aces count as 1 or 11 (auto-optimized)
- Player can **Hit** or **Stand**
- Dealer hits until score ≥ 17
- Automatic win/loss detection:
  - Blackjack
  - Bust
  - Score comparison

---

## 🛠️ How the Game Works
1. Deck is created and shuffled
2. Initial cards are dealt to player and dealer
3. Player chooses to hit or stand
4. Dealer reveals cards and follows dealer policy
5. Winner is determined

---

## ▶️ How to Run

```bash
python src/blackjack.py

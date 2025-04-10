# 📚 Flashy - Language Learning Flashcard App

Flashy is a simple and interactive flashcard-style app built using **Python** and **Tkinter**.  
It helps users learn vocabulary from one language to another — for example, learning English words with their Hindi meanings.

## 🧠 How It Works

- Flashcards show one word at a time from the known language (e.g., English).
- After a few seconds, the card flips to reveal the translated word (e.g., Hindi).
- Users can click ✅ or ❌ to move to the next word.
- Words are randomly chosen from a CSV file.
- The app automatically flips cards after a delay for passive learning.

## 💻 Technologies Used

- Python 3.x
- Tkinter (GUI)
- Pandas (for reading CSV)
- CSV file for vocabulary data
- Images for card front/back and buttons

## 📦 Requirements

Install the dependencies using:

```bash
pip install pandas
```
📄 How to Use  
```bash  
git clone https://github.com/RohitKumarChaudhari/flashy.git
cd flashy
python main.py
```

📝 Customization  
- Replace the CSV file to learn any other language pairs.
- Add new words to the CSV file.
- Change images in the /images/ folder to customize the UI.

🎯 Features  
- Random word display
- Easy to add new words
- Auto-save support (optional)
- Great for beginners learning new vocabulary

Built with ❤️ by Rohit using Python and Tkinter.


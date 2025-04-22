# UNIX Systems Programming - Locale Utility Assignment

This Python script is designed for a UNIX Systems Programming assignment. It reads a file containing locale and charmap information and displays specific data based on command-line options. The script handles file reading, data filtering, and summarizing locales and charmaps related to different languages.

---

## 🔧 File Structure

- `locale.py`: The main script (core of the assignment)
- `locale.txt`: Example input file containing locale and charmap entries in CSV format

---

## 🧪 Usage

Run the script using the following syntax:

```bash
python3 locale.py [OPTION] [FILENAME] [LANGUAGE (optional)]
```

### Available Options:

| Option    | Description                                         |
|-----------|-----------------------------------------------------|
| `-a`      | Lists available locales                             |
| `-m`      | Lists available charmaps                            |
| `-l <language>` | Shows number of locales and charmaps for given language |
| `-v`      | Displays student information (name, ID, date)       |

---

## ✅ Example Commands

```bash
python3 locale.py -a locale.txt
python3 locale.py -m locale.txt
python3 locale.py -l ja locale.txt
python3 locale.py -v
```

---

## 👤 Student Information

- **Name**: Emi Sekikawa  
- **Student ID**: 14507608  
- **Date of Completion**: 17 May 2024  
- **Subject**: UNIX Systems Programming  

---

## 📌 Notes

- The input file must be in comma-separated (CSV) format.
- Basic error handling is implemented to notify users of invalid options or unreadable files.

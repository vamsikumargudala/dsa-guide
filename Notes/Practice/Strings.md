## Python `str` Class Overview

Python's `str` class is a powerful and flexible tool for handling text. Strings are **immutable sequences of Unicode code points**, meaning each character is stored as a unique Unicode value. Because they are immutable, any operation that modifies a string actually returns a new string.

### 🔹 String Characteristics

- **Immutable**: Strings cannot be changed after creation.
- **Indexed**: Characters can be accessed using 0-based (left) or -1-based (right) indexing.
- **Iterable**: You can loop through strings using `for char in str` or `for index, char in enumerate(str)`.
- **Concatenation**: Use `+` or `''.join(iterable)` for joining strings.
- **Unicode**: Strings support multilingual text and symbols (e.g., emojis) through Unicode code points.

A Unicode code point is a unique number assigned to every character in the Unicode standard. This includes letters, digits, punctuation, symbols, and emojis from almost every writing system in the world.

Each code point is written as U+ followed by a hexadecimal number (e.g., U+1F600 for 😀).
Code points are abstract values; how they're stored in memory depends on the encoding (like UTF-8 or UTF-16).
In most programming languages, strings are sequences of these code points, not just bytes or ASCII characters.
Example:
The letter A has the code point U+0041.
The emoji 😀 has the code point U+1F600.

Gotcha:
Some characters (like emojis) use more than one byte in memory because their code points are higher than U+007F.

## Common `str` Methods

### `str.title()`
Capitalizes the first character of each word. Word boundaries depend on the locale and language rules.

```python
'мужчина в шляпе'.title()      # 'Мужчина В Шляпе'
'모자를 쓴 남자'.title()         # '모자를 쓴 남자'
'the man in the hat.'.title()  # 'The Man In The Hat.'
```

### `str.endswith(suffix)`

Returns `True` if the string ends with the given `suffix`.

```python
'My heart breaks. 💔'.endswith('💔')    # True
'cheerfulness'.endswith('ness')        # True
'Do you want to 💃?'.endswith('💃')      # False
'...lazy dog.'.endswith('dog')         # False (punctuation matters)
```

---

### `str.strip([chars])`

Removes leading and trailing characters specified in `chars`. If omitted, removes whitespace.

```python
'https://unicode.org/emoji/'.strip('/stph:')  # 'unicode.org/emoji'
'   🐪🐪🐪🌟🐪🐪🐪   '.strip()                   # '🐪🐪🐪🌟🐪🐪🐪'
'оправдание'.strip('еина')                   # 'оправд'
'unaddressed'.strip('dnue')                  # 'address'
'  unaddressed  '.strip('dnue ')             # 'address'
```

---

### `str.replace(old, new)`

Replaces all occurrences of `old` with `new`.

```python
quote = '''
"Just the place for a Snark!" the Bellman cried,
   As he landed his crew with care;
Supporting each man on the top of the tide
   By a finger entwined in his hair.

"Just the place for a Snark! I have said it twice:
   That alone should encourage the crew.
Just the place for a Snark! I have said it thrice:
   What I tell you three times is true."
'''

quote.replace('Snark', '🐲')  # Replaces all instances of 'Snark' with '🐲'

'bookkeeper'.replace('kk', 'k k')  # 'book keeper'
```

---

## Method Summary

| Method        | Description                                          |
| ------------- | ---------------------------------------------------- |
| `.title()`    | Capitalizes the first letter of each word            |
| `.endswith()` | Checks if string ends with the specified suffix      |
| `.strip()`    | Removes specified characters from both ends          |
| `.replace()`  | Replaces all occurrences of a substring with another |

---

## Notes

* All string methods return a **new string** and do **not** modify the original.
* Characters like emojis and non-Latin alphabets are fully supported thanks to Unicode.


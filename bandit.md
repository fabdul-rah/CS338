# Feraidon AbdulRahimzai

**Date:** Sep 16, 2025
**Course:** Computer Security
**Challenge:** OverTheWire — Bandit

---

## Level 0

**Steps**:

Login to Bandit using the following UNIX command:

```bash
ssh -p 2220 bandit0@bandit.labs.overthewire.org
```

The password is given on the game's introduction page as: `bandit0`.

---

## Level 0 → 1

**Steps:**

Open `readme` using:

```bash
cat readme
```

The password for the next level is displayed.

**Password:** `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`

---

## Level 1 → 2

**Steps:**

The file name contains a single dash (`-`) which can be interpreted as stdin. One approach is to use `rev -` to read and reverse the contents without treating `-` as an option, and then reverse again to recover the original.

What I used:

```bash
rev - | rev
```

**Password:** `263JGJPfgU6LtdEvgfWU1XP5yac29mFx`

---

## Level 2 → 3

**Steps:**

![][screenshots-bandit/Screenshot 2025-09-16 at 8.45.23 PM.png]

**Password:** `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx`

---

## Level 3 → 4

**Steps:**

![][screenshots-bandit/Screenshot 2025-09-16 at 8.50.22 PM.png]
**Password:** `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`

---

## Level 4 → 5

**Steps:**

![][screenshots-bandit/Screenshot 2025-09-16 at 9.09.47 PM.png]
**Password:** `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

---

## Level 5 → 6

**Steps:**

![][screenshots-bandit/Screenshot 2025-09-16 at 9.34.25 PM.png]
**Password:** `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

---

## Level 6 → 7

**Steps:**

Used `find` to search for files of a specific size (33 bytes):

```bash
find -type f -size 1033c
```
![][screenshots-bandit/Screenshot 2025-09-17 at 10.31.29 AM.png]

This revealed the directory containing the password file; navigating one directory deeper and repeating the command located the file with the password.

**Password:** `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

---

## Level 7 → 8

**Steps:**

Concatenate data.txt and then using command f

Then find the line corresponding to the word `millionth` and extract the associated password.

![][screenshots-bandit/Screenshot 2025-09-17 at 10.37.30 AM.png]

**Password:** `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

---

## Level 8 → 9

**Steps / Output:**

Tried sorting and finding unique lines:

```bash
sort data.txt | uniq -u
```

The unique password found was:

**Password:** `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

---

## Level 9 → 10

**Steps:**

Used the `strings` utility to extract printable strings from a binary/text file:

```bash
strings data.txt
```

**Password:** `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`

---

## Level 10 → 11

**Steps:**

Listed and examined `data.txt`:

```bash
cat data.txt
# shows Base64 content: VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==
```

Decoded the Base64 using:

```bash
base64 -d data.txt
```

Result:

```
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```

**Password:** `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`

---

## Level 11 → 12

**Steps:**

The file contained a ROT13-encoded line. Using `tr` to perform ROT13 revealed the password:

```bash
cat data.txt
# Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4

tr 'A-Za-z' 'N-ZA-Mn-za-m' <<< "7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4"
# returns 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```

**Password:** `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`

---

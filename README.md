## Data Collection & Visualization of Hungarian NB1 Football from 1980-2022

- Data was sourced from [magyarfutball.hu](https://www.magyarfutball.hu/hu/merkozesek)
- The script uses BeautifulSoup4 to extract data from the html pages
- Parses them into a MatchResults list which contains:
  - Match season and round (forduló)
  - Match date and time
  - Match location and participating teams
  - Match results
  - Attendance (Viewers who attended locally) _(where data is available)_
- The results then get parsed into a Pandas DataFrame where additional modifications can be done
  - Also saves the dataframe to a .csv file

- Can be modified for other year ranges as well
---

### Using the extracted data we can quickly create visualizations using [DeepNote](https://deepnote.com/) (or a visualization library of our choice) to make observations

![image](https://github.com/hanubence/foci/assets/32911312/e77682e3-ad86-4f7c-a983-904ec7440b64)

[Interactive version](https://embed.deepnote.com/2b023a1e-30da-4350-99df-8286fc144bcb/8e3b20be8c024ac298f0e44828f6c19a/f087c748893346a3bbf458690da2d4f6?height=507)

![image](https://github.com/hanubence/foci/assets/32911312/d38e8fd7-133f-4429-a697-44abff2a6af3)

The COVID-19 Pandemic caused attendance to decrease a lot (probably near zero due to averaging)
[Interactive version](https://embed.deepnote.com/2b023a1e-30da-4350-99df-8286fc144bcb/8e3b20be8c024ac298f0e44828f6c19a/6d5d574c01564d77bc1f29284fb5a47a?height=550)

#### [Link to full DeepNote workbook](https://deepnote.com/workspace/foci-98c8-b0fcb992-1465-4b5f-8501-f6c3a51e83a3/project/Foci-2b023a1e-30da-4350-99df-8286fc144bcb/notebook/Notebook%201-8e3b20be8c024ac298f0e44828f6c19a)

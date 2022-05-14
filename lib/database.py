import sqlite3

class database:
    def __init__(self):
        try:
            self.connection = sqlite3.connect("./db/books.db")
        except:
            print("")
        self.cursor = self.connection.cursor()
        sql = "PRAGMA foreign_keys = ON;"
        self.cursor.execute(sql)

    def new_book(self, name, img_path = None):
        if img_path is not None and img_path != '': 
            img = read_img(img_path)
            sql = 'INSERT INTO BOOK (TITLE, IMG) VALUES(?,?);'
            self.cursor.execute(sql, (str(name), img))
        else:
            self.cursor.execute("INSERT INTO BOOK (TITLE)  VALUES ('" +name+ "');")
        return self.get_id('BOOK')

    def new_page(self, book_id, img_path = None):
        if img_path is not None: img = read_img(img_path)
        sql = 'SELECT COUNT(ID) FROM PAGES WHERE BOOK = ' + str(book_id) + ';'
        try:
            num = self.cursor.execute(sql).fetchall()
            if len(num) > 0:
                num = num[0][0] + 1
            else: num = 1
        except:
            print("Something went wrong!")
            return
        if img_path is not None:
            sql = 'INSERT INTO PAGES (IMG, BOOK, NUM) \
                        VALUES(?, ?, ?);'
            self.execute(sql,(img, book_id, num))
        else:
            sql = 'INSERT INTO PAGES (BOOK, NUM) \
                        VALUES(?, ?);'
            self.execute(sql, (book_id, num))
        return self.get_id('PAGES')

    def get_id(self, table_name):
        sql = 'SELECT MAX(ID) FROM '+ table_name +';'
        id = self.cursor.execute(sql).fetchall()
        return id[0][0]

    def commit(self):
        self.connection.commit()

    def new_page_text(self, txt_pt, txt_en, page_id):
        sql = 'INSERT INTO PAGE_CONTENTS (PT, EN, PAGEID) VALUES (?, ?, ?);'
        self.execute(sql, (txt_pt, txt_en, page_id))
    
    def new_word(self, pt, en, vid_path):
        sql = 'INSERT INTO WORDS(WORD_EN, WORD_PT, FIG_PATH) VALUES (?, ?, ?);'
        
        self.cursor.execute(sql, (upper(pt), upper(en), vid_path))

    def execute(self, sql, opt):
        try:
            if opt == None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, opt)
        except:
            print("Something went wrong!")
    def get_pages(self, book_id):
        sql = 'SELECT * FROM PAGES WHERE BOOK =' + str(book_id)+ ';'
        pages = self.cursor.execute(sql).fetchall()
        return pages
    def get_page(self, page_id):
        sql = 'SELECT * FROM PAGES WHERE ID =' + str(page_id)+ ';'
        page = self.cursor.execute(sql).fetchall()
        return page
    def get_page_text(self, page_id):
        sql = 'SELECT * FROM PAGE_CONTENTS WHERE PAGEID =' + str(page_id)+ ';'
        content = self.cursor.execute(sql).fetchall()
        if len(content) > 0:
            return content[0]
        else:
            return content
    def get_books(self, book_id = None):
        if book_id is not None:
            sql = 'SELECT * FROM BOOK WHERE ID = '+ str(book_id)+';'
        else:
            sql = 'SELECT * FROM BOOK;'
        books = self.cursor.execute(sql).fetchall()
        return books
    def get_word(self, word):
        sql = 'SELECT * FROM WORDS WHERE WORD_EN = "' + word +'";'
        ans = self.cursor.execute(sql).fetchall()
        if len(ans) > 0: return ans[0]
        else: return ans
    def disconnect(self):
        self.connection.close()

    
def read_img(img_path):
    with open(img_path, 'rb') as file:
        blob = file.read()
    return blob

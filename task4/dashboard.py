import sys
import mysql.connector
import csv
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QTableWidget, QTableWidgetItem, QGridLayout, 
    QTextEdit, QSizePolicy, QLineEdit,QFileDialog
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CineScope – Dashboard")
        self.setMinimumSize(1200, 800)
        self.setStyleSheet("background-color: #121212; color: white; padding: 20px;")
        self.init_ui()
        self.connection = None
        self.cursor = None
        self.connect_to_db()
    def connect_to_db(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="prajwal",
                password="Fevicol!1",
                database="movies_db"
            )
            self.cursor = self.connection.cursor(dictionary=True)
            self.output_console.append("Connected to database successfully.")
        except mysql.connector.Error as err:
            self.output_console.append(f"Error: {err}")
    
    def populate_table(self, data):
        if not data:
            self.output_console.append("No data to display.")
            return
        self.table.clear()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))
        self.table.setHorizontalHeaderLabels(data[0].keys())
        for row_idx, row_data in enumerate(data):
            for col_idx, (col_name, col_value) in enumerate(row_data.items()):
                item = QTableWidgetItem(str(col_value))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.table.setItem(row_idx, col_idx, item)
        self.output_console.append("Table populated with data.")
    

        

    def init_ui(self):
        self.selected_columns = ["Series_Title", "Released_Year", "Genre", "IMDB_Rating", "Director", "Star1"]
        self.column_buttons = {}
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        # Header
        header = QLabel("🎬 CineScope Dashboard")
        header.setFont(QFont("Arial", 24, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        header.setFixedHeight(80)
        main_layout.addWidget(header)

        split_layout = QHBoxLayout()

        # Left Panel
        left_container = QVBoxLayout()
        left_container.setSpacing(10)
        left_container.setAlignment(Qt.AlignTop)

        # Search buttons
        search_heading = QLabel("Search By")
        search_heading.setFont(QFont("Arial", 18, QFont.Bold))
        left_container.addWidget(search_heading)

        search_buttons = [
            ("Genre", "genre"),
            ("Year", "year"),
            ("Rating", "rating"),
            ("Director", "director"),
            ("Actor", "actor"),
        ]

        search_grid = QGridLayout()
        for index, (label, mode) in enumerate(search_buttons):
            btn = QPushButton(label)
            btn.setStyleSheet(self.get_button_style(False))
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(lambda _, m=mode: self.set_search_mode(m))
            row, col = divmod(index, 2)
            search_grid.addWidget(btn, row, col)
        left_container.addLayout(search_grid)

        # Column selection
        column_heading = QLabel("Select Columns")
        column_heading.setFont(QFont("Arial", 18, QFont.Bold))
        left_container.addWidget(column_heading)

        column_buttons = [
            ("Title", "Series_Title"),
            ("Year", "Released_Year"),
            ("Genre", "Genre"),
            ("Rating", "IMDB_Rating"),
            ("Director", "Director"),
            ("Stars", "Star1"),
        ]

        column_grid = QGridLayout()
        for index, (label, col) in enumerate(column_buttons):
            btn = QPushButton(label)
            btn.setStyleSheet(self.get_button_style(True if col in self.selected_columns else False))
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(lambda _, c=col: self.toggle_column(c))
            self.column_buttons[col] = btn
            row, col = divmod(index, 2)
            column_grid.addWidget(btn, row, col)
        left_container.addLayout(column_grid)
        
        


        # Search input
        self.query_input = QLineEdit()
        self.query_input.setPlaceholderText("Enter search term")
        self.query_input.setStyleSheet("background-color: #1e1e1e; color: white; padding: 5px; border: 1px solid #444;")
        left_container.addWidget(self.query_input)

        # Action buttons
        action_layout = QHBoxLayout()
        search_btn = QPushButton("Search")
        search_btn.setStyleSheet("background-color: #e50914; color: white; padding: 6px; border-radius: 5px;")
        search_btn.clicked.connect(self.execute_search)
        action_layout.addWidget(search_btn)

        export_btn = QPushButton("Export CSV")
        export_btn.setStyleSheet("background-color: #1f1f1f; color: white; padding: 6px; border-radius: 5px;")
        export_btn.clicked.connect(self.export_csv)
        action_layout.addWidget(export_btn)
        left_container.addLayout(action_layout)

        # Right Panel
        right_side_layout = QVBoxLayout()
        right_side_layout.setSpacing(10)

        # Table
        self.table = QTableWidget()
        self.table.setStyleSheet("""
            QTableWidget {
                color: white;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: white;
                color: black;
                padding: 4px;
            }
        """)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Output console
        self.output_console = QTextEdit()
        self.output_console.setPlaceholderText("Results will appear here...")
        self.output_console.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: white;
                border: 1px solid #444;
                padding: 5px;
            }
        """)
        self.output_console.setFixedHeight(100)

        right_side_layout.addWidget(self.table)
        right_side_layout.addWidget(self.output_console)

        split_layout.addLayout(left_container, 2)
        split_layout.addLayout(right_side_layout, 8)
        main_layout.addLayout(split_layout)
        self.setLayout(main_layout)

    def get_button_style(self, is_selected):
        if is_selected:
            return """
                QPushButton {
                    background-color: #ffcc00;
                    border: 1px solid #ff9900;
                    border-radius: 3px;
                    padding: 6px;
                }
            """
        else:
            return """
                QPushButton {
                    background-color: #1f1f1f;
                    border: 1px solid #333;
                    border-radius: 3px;
                    padding: 6px;
                }
                QPushButton:hover {
                    background-color: #333;
                }

            """
   
          

    def set_search_mode(self, mode):
        self.search_mode = mode
        if mode == "genre":
            self.query_input.setPlaceholderText("Enter genre")
        elif mode == "year":
           self.query_input.setPlaceholderText("Enter year")
        elif mode == "rating":
            self.query_input.setPlaceholderText("Enter minimum rating")
        elif mode == "director":
            self.query_input.setPlaceholderText("Enter director name")
        elif mode == "actor":
            self.query_input.setPlaceholderText("Enter actor name")
        self.output_console.append(f"Search mode set to: {mode}")
        self.output_console.append(f"Search mode set to: {mode}")


    def toggle_column(self, column):
        if column in self.selected_columns:
            self.selected_columns.remove(column)
            self.column_buttons[column].setStyleSheet(self.get_button_style(False))
        else:
            self.selected_columns.append(column)
            self.column_buttons[column].setStyleSheet(self.get_button_style(True))
        self.output_console.append(f"Selected columns: {', '.join(self.selected_columns)}")


    def execute_search(self):
        self.output_console.append("Executing search...")
        search_value = self.query_input.text().strip()
        columns= self.selected_columns if self.selected_columns else["title"]
        if self.search_mode == "year":
            if not search_value.isdigit() or len(search_value) != 4:
                self.output_console.append("Please enter a valid year.")
                return
            query = f"SELECT {', '.join(columns)} FROM movies WHERE Released_Year >= %s"
            params = (search_value,)
        elif self.search_mode == "genre":
            query= f"SELECT {', '.join(columns)} FROM movies WHERE Genre LIKE %s" 
            params = (f"%{search_value}%",)
        elif self.search_mode == "rating":
            if not search_value.replace('.','',1).isdigit() or not (0 <= float(search_value) <= 10):
                self.output_console.append("Please enter a valid rating between 0 and 10.")
                return
            query= f"SELECT {', '.join(columns)} FROM movies WHERE IMDB_Rating >= %s"
            params = (search_value,)
        elif self.search_mode == "director":
            query= f"SELECT {', '.join(columns)} FROM movies WHERE Director LIKE %s"
            params = (f"%{search_value}%",)
        elif self.search_mode == "actor":
            query= f"SELECT {', '.join(columns)} FROM movies WHERE Star1 LIKE %s OR Star2 LIKE %s OR Star3 LIKE %s"
            params = (f"%{search_value}%", f"%{search_value}%", f"%{search_value}%")
        else:
            self.output_console.append("Please enter a search term.")
            return       
        self.cursor.execute(query, params)
        results = self.cursor.fetchall()
        self.output_console.append(f"Found {len(results)} results.")
        self.populate_table(results)
        
            

    def export_csv(self):
        self.output_console.append("Exporting to CSV...")
        row_count = self.table.rowCount()
        col_count = self.table.columnCount()
        if row_count == 0 or col_count == 0:
            self.output_console.append("No data to export.")
            return
        with open("exported_data.csv", "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
        header = [self.table.horizontalHeaderItem(col).text() 
                  if self.table.horizontalHeaderItem(col) 
                  else "" 
                  for col in range(col_count)
                  
                  ]
        writer.writerow(header)
        for row in range(row_count):
            row_data = [
                self.table.item(row, col).text() 
                if self.table.item(row, col) 
                else ""
                for col in range(col_count)
            ]
            writer.writerow(row_data)
        self.output_console.append("Data exported to exported_data.csv.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())

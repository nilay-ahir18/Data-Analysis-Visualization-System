import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:

    def __init__(self):
        self.df = None

    
    def load_data(self):
        path = input("Enter CSV file path: ")
        try:
            self.df = pd.read_csv(path)
            print("Dataset loaded successfully!\n")
        except Exception as e:
            print("Error loading file:", e)

    
    def explore_data(self):
        if self.df is None:
            print("Load dataset first!\n")
            return

        print("\n1. First 5 rows")
        print("2. Last 5 rows")
        print("3. Column names")
        print("4. Data types")
        print("5. Basic info")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print(self.df.head())
        elif choice == 2:
            print(self.df.tail())
        elif choice == 3:
            print(self.df.columns)
        elif choice == 4:
            print(self.df.dtypes)
        elif choice == 5:
            print(self.df.info())

    
    def dataframe_operations(self):
        if self.df is None:
            print("Load dataset first!\n")
            return

        print("\n1. Sort Data")
        print("2. Filter Data")

        choice = int(input("Enter choice: "))

        if choice == 1:
            col = input("Enter column name: ")
            print(self.df.sort_values(by=col))
        elif choice == 2:
            col = input("Column name: ")
            val = input("Value: ")
            print(self.df[self.df[col] == val])

    
    def handle_missing(self):
        if self.df is None:
            print("Load dataset first!\n")
            return

        print("\n1. Show missing values")
        print("2. Fill with mean")
        print("3. Drop missing rows")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print(self.df.isnull().sum())
        elif choice == 2:
            self.df.fillna(self.df.mean(numeric_only=True), inplace=True)
            print("Filled with mean")
        elif choice == 3:
            self.df.dropna(inplace=True)
            print("Rows dropped")

    
    def statistics(self):
        if self.df is None:
            print("Load dataset first!\n")
            return

        print(self.df.describe())

    
    def visualize(self):
        if self.df is None:
            print("Load dataset first!\n")
            return

        print("\n1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Heatmap")

        choice = int(input("Enter choice: "))

        if choice == 1:
            col = input("Column name: ")
            self.df[col].value_counts().plot(kind='bar')
            plt.title("Bar Plot")
            plt.show()

        elif choice == 2:
            col = input("Column name: ")
            self.df[col].plot()
            plt.title("Line Plot")
            plt.show()

        elif choice == 3:
            x = input("X column: ")
            y = input("Y column: ")
            plt.scatter(self.df[x], self.df[y])
            plt.title("Scatter Plot")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()

        elif choice == 4:
            col = input("Column name: ")
            self.df[col].value_counts().plot(kind='pie', autopct='%1.1f%%')
            plt.title("Pie Chart")
            plt.show()

        elif choice == 5:
            col = input("Column name: ")
            self.df[col].plot(kind='hist')
            plt.title("Histogram")
            plt.show()

        elif choice == 6:
            sns.heatmap(self.df.corr(numeric_only=True), annot=True)
            plt.title("Heatmap")
            plt.show()

    
    def save_plot(self):
        name = input("Enter file name (e.g., plot.png): ")
        plt.savefig(name)
        print("Saved successfully!")


def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n===== Data Analysis & Visualization =====")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Data Operations")
        print("4. Handle Missing Data")
        print("5. Descriptive Statistics")
        print("6. Visualization")
        print("7. Save Plot")
        print("8. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            analyzer.load_data()
        elif choice == 2:
            analyzer.explore_data()
        elif choice == 3:
            analyzer.dataframe_operations()
        elif choice == 4:
            analyzer.handle_missing()
        elif choice == 5:
            analyzer.statistics()
        elif choice == 6:
            analyzer.visualize()
        elif choice == 7:
            analyzer.save_plot()
        elif choice == 8:
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
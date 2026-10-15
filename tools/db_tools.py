from langchain.tools import BaseTool
import sqlite3

class InstitutionsDBTool(BaseTool):
    name: str = "institutions_db_tool"
    description: str = "Useful for answering questions about educational institutions, government offices, and other institutional information in Bangladesh."

    def _run(self, query: str) -> str:
        try:
            conn = sqlite3.connect("databases/institutions.db")
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            conn.close()
            return str(results) if results else "No data found."
        except Exception as e:
            return f"Error: {str(e)}"

class HospitalsDBTool(BaseTool):
    name: str = "hospitals_db_tool"
    description: str = "Useful for answering questions about hospitals, bed capacity, doctors, and medical facilities in Bangladesh."

    def _run(self, query: str) -> str:
        try:
            conn = sqlite3.connect("databases/hospitals.db")
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            conn.close()
            return str(results) if results else "No data found."
        except Exception as e:
            return f"Error: {str(e)}"

class RestaurantsDBTool(BaseTool):
    name: str = "restaurants_db_tool"
    description: str = "Useful for answering questions about restaurants, cuisine types, ratings, and locations in Bangladesh."

    def _run(self, query: str) -> str:
        try:
            conn = sqlite3.connect("databases/restaurants.db")
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            conn.close()
            return str(results) if results else "No data found."
        except Exception as e:
            return f"Error: {str(e)}"
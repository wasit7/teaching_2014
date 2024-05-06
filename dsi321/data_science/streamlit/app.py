import streamlit as st
import pandas as pd
import sqlalchemy
from io import StringIO

# Connection string to the PostgreSQL database
DATABASE_URL = "postgresql+psycopg2://user:password@postgres:5432/datascience"
# DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/datascience"

# Setup database connection
@st.cache_resource
def get_database_connection():
    engine = sqlalchemy.create_engine(DATABASE_URL)
    return engine.connect()

# Fetch dataset names from the database
@st.cache_data
def get_datasets(_conn):
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
    return pd.read_sql(query, _conn)

# Fetch metadata for a specific table
@st.cache_data
def get_table_description(_conn, table_name):
    query = f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'"
    return pd.read_sql(query, _conn)

# Load data from a specific table
@st.cache_data
def load_data(_conn, table_name):
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, _conn)

def main():
    st.title("Dataset Explorer")

    conn = get_database_connection()
    datasets = get_datasets(conn)
    dataset_names = datasets['table_name'].tolist()

    if not dataset_names:
        st.error("No datasets found in the database.")
        return

    dataset_selected = st.sidebar.selectbox("Select a dataset", dataset_names)

    if dataset_selected:
        # Display metadata
        metadata = get_table_description(conn, dataset_selected)
        if not metadata.empty:
            st.write(f"Metadata for {dataset_selected}:")
            st.dataframe(metadata)
        else:
            st.write("No metadata available.")

        # Load and display data
        data = load_data(conn, dataset_selected)
        if not data.empty:
            st.write("Data Preview:")
            st.dataframe(data.head())

            # Basic EDA options
            if st.button("Show Info"):
                buffer = StringIO()
                data.info(buf=buffer)
                s = buffer.getvalue()
                st.text(s)

            if st.button("Show Distribution"):
                st.write(data.describe())
        else:
            st.write("No data available for this dataset.")

if __name__ == "__main__":
    main()

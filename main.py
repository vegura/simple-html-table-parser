import requests
import bs4
import numpy as np
import csv

table_content_destination = "out.csv"


def get_page_raw():
    return requests.get("https://www.worldfootball.net/schedule/bundesliga-2021-2022-spieltag/31/").text


def parse_html_table(html_text, table_order_number=0):
    bs_obj = bs4.BeautifulSoup(html_text, features="html.parser")
    data_tables = bs_obj.find_all("table", attrs={"class": "standard_tabelle"})

    first_table = data_tables[table_order_number]
    table_content_list = []
    for table_row in first_table.find_all("tr"):
        row_content = []
        for table_cell in table_row.find_all("td"):
            row_content.append(table_cell.text.strip())
        row_content = row_content[:-1]
        table_content_list.append(row_content)
    return table_content_list


def save_list_table_as_csv(table_list):
    table_array = np.array(table_list, dtype=str)
    np.savetxt(table_content_destination, table_array, delimiter=",", newline="\n", fmt="%s")


def save_list_csv(table_data: list, writing_type='a'):
    with open(table_content_destination, 'a') as result_file:
        csv_result_file = csv.writer(result_file)
        csv_result_file.writerows(table_data)


def main():
    page_content_raw = get_page_raw()
    main_result_table = parse_html_table(page_content_raw)
    team_details_table = parse_html_table(page_content_raw, 1)
    save_list_csv(main_result_table)
    save_list_csv(team_details_table)


if __name__ == "__main__":
    main()
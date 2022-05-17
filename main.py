import requests
import bs4
import csv


def get_page_raw(source_page):
    return requests.get(source_page).text


def parse_html_table(html_text, table_order_number=0):
    bs_obj = bs4.BeautifulSoup(html_text, features="html.parser")
    data_tables = bs_obj.find_all("table", attrs={"class": "standard_tabelle"})

    first_table = data_tables[table_order_number]
    table_content_list = []
    for table_row in first_table.find_all("tr"):
        row_content = []
        for table_cell in table_row.find_all("td"):
            row_content.append(table_cell.text.strip())
        table_content_list.append(row_content)
    return table_content_list


def save_list_csv(table_data: list, filename, writing_type='a'):
    with open(filename, 'a') as result_file:
        csv_result_file = csv.writer(result_file)
        csv_result_file.writerows(table_data)


def read_league_links():
    leagues_list = []
    with open("leagues.txt", "r") as leagues_pages_file:
        leagues = leagues_pages_file.readlines()
        for league in leagues:
            leagues_list.append(league.strip("\n"))
    return leagues_list


def main():
    league_page_links = read_league_links()
    for league_page_link in league_page_links:
        page_content_raw = get_page_raw(league_page_link)
        main_result_table = parse_html_table(page_content_raw)
        team_details_table = parse_html_table(page_content_raw, 1)

        data_file_name = league_page_link.split("/")[-1] + ".csv"  # page name
        print(data_file_name)

        save_list_csv(main_result_table, data_file_name)
        save_list_csv(team_details_table, data_file_name)


if __name__ == "__main__":
    main()
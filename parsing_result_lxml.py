import lxml.html as html
import requests as r
import main as base_actions

def main():
    base_actions.get_page_raw()
    parsed_document = html.fromstring(resp.text)
    xpath_el = "/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div[1]/div[7]/div/table[1]/tbody/tr[1]/th[1]"
    elements = parsed_document.xpath(xpath_el)

    elements = [text for text in elements if text != u'\xa0']
    print('\n'.join(elements))


if __name__ == "__main__":
    main()
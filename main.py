import sys

from helpers.parse_links import parse_links
from helpers.skills import get_all_skills
from helpers.write_results import  write_results
from helpers.get_job_links import get_job_links
from pages.SearchPage import SearchPage


# skills = ['Тестирование', 'Linux', 'Debian', 'TCP/IP', 'Qt', 'C++', 'Python', 'Bash', 'SQL', 'PostgreSQL', 'Французский — A1 — Начальный', 'Английский — B2 — Средне-продвинутый', 'Docker', 'Git', 'PostgreSQL', 'Atlassian Jira', 'Bash', 'Linux', 'SQL', 'Ручное тестирование', 'Написание автотестов', 'REST API', 'Python', 'Test case', 'Kibana', 'Kubernetes', 'Gitlab', 'Git', 'Ручное тестирование', 'Автоматизированное тестирование', 'Postman', 'Python', 'QA', 'Postman', 'Swagger', 'UI', 'DevTools', 'Zephyr Scale', 'HTTP', 'Pytest', 'Selenium', 'Playwright', 'Python', 'Docker', 'k8s', 'Python, Bash, JavaScript, Groovy, Java, C#', 'Selenium, HP UFT, Cucumber, JUnit, TestNG, Espresso, Earl Grey, API, TestComplete', 'SoapUI, rfhutil, MQ, Fiddler', 'Oracle, MySQL, MS SQL Server, PostgreSQL, GridGain, Firebird', 'Altova XMLSpy', 'Git', 'Функциональное тестирование', 'Linux', 'HTML', 'Beta-тестирования', 'Проведение тестирований', 'GitHub', 'Удаленная работа', 'Основы программирования', 'Ручное тестирование', 'PHP', 'Python', 'Автоматизированное тестирование', 'Python', 'Linux', 'Docker', 'Pytest', 'Unit Testing', 'CI/CD', 'QA', 'Linux', 'Python', 'Bash', 'Ручное тестирование', 'Smoke-тестирование', 'Регрессионное тестирование', 'JSON API', 'Английский — A2 — Элементарный', 'Python', 'Наставничество', 'PostgreSQL', 'SQL', 'FastAPI', 'Django Framework', 'NoSQL', 'Redis', 'MongoDB', 'gRPC', 'TDD', 'OWASP Top 10', 'JWT', 'OAuth', 'CI/CD', 'GitLab CI', 'GitHub', 'Kubernetes', 'MLflow', 'PyTorch', 'TensorFlow', 'Clickhouse', 'Postman', 'Devtools', 'Swagger', 'Ручное тестирование', 'Автоматизированное тестирование', 'CI/CD', 'Python', 'JavaScript', 'TypeScript', 'Написание автотестов', 'Контроль качества', 'Тестирование', 'Test case', 'QA', 'Atlassian Jira', 'Проведение тестирований', 'Ручное тестирование', 'TestIT', 'AutoIt', 'Функциональное тестирование', 'Python', 'Pytest', 'Postman', 'Git', 'ELK', 'Grafana', 'QA', 'Python', 'Pytest', 'Allure', 'Linux', 'Windows Os', 'Git', 'SQL', 'Docker', 'Python', 'Linux', 'Pytest', 'MS SQL', 'Python', 'Docker', 'PostgreSQL', 'Kafka', 'Pytest', 'Selenium', 'Playwright', 'Тестирование', 'Linux', 'Git', 'SQL', 'Python', 'Управление командой', 'Написание автотестов', 'Pytest', 'Автоматизированное тестирование', 'Нагрузочное тестирование', 'Регрессионное тестирование', 'Python', 'Тест-дизайн', 'GitLab CI', 'SQL', 'API', 'JavaScript', 'Тестирование', 'REST API', 'CI/CD', 'QA', 'Test case', 'SQL', 'Java', 'AWS', 'Cucumber', 'Английский — B2 — Средне-продвинутый', 'Python', 'Django Framework', 'SQL', 'PostgreSQL', 'Тестирование', 'Функциональное тестирование', 'Postman', 'Swagger', 'Charles', 'Fiddler', 'API', 'QA', 'Linux', 'Тестирование API', 'SQL', 'CI/CD', 'Ручное тестирование', 'Английский язык', 'SQL', 'PostgreSQL', 'Atlassian Confluence', 'Python', 'Написание автотестов', 'Обучение и развитие', 'Test case', 'Use case', 'API', 'Python', 'Функциональное тестирование', 'Python', 'Automation testing', 'Git', 'Kotlin', 'REST API', 'Английский — B2 — Средне-продвинутый', 'SQL', 'Linux', 'Python', 'Appium', 'Тестирование', 'Автоматизация', 'Тестирование мобильных приложений', 'Ручное тестирование', 'Обеспечение качества', 'QA']
# print(json.dumps(result, indent=4, ensure_ascii=False))


def main():

    query = sys.argv[1]
    print('Идет поиск, не прерывайте выполнение программы')

    # links = get_job_links(query)
    search_page = SearchPage(query)
    print(search_page.url)
    # parsed_data = parse_links(search_page.links)
    # skills = get_all_skills(parsed_data)

    # write_results(parsed_data, skills)

    print('LINKS', search_page.links)
    print('PAGES_COUNT', search_page.pages_count)

    print('Результаты сформированы в папке results')

if __name__ == '__main__':
    main()
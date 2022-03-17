Jeśli tworzymy osobny folder z testami to trzeba zrobić z niego pakiet.
Pakiet tworzymy dodając w folerze pusty plik `__init__.py`.

`python -m pytest` lub (różnica poniżej) `pytest`
Uruchomi wszystkie testy, które są w plikach zaczynających się od test*
i metodach w tych plikach zaczynających się od test*.

`python -m pytest -v`
To samo ale wyświeli konkretne testy.

`python -m pytest -v ksiazka_py/testy15`
Uruchomi testy tylko z tego katalogu i podrzędnych.

`python -m pytest -v .\ksiazka_py\testy15\py_17flatten_pytest.py`
Uruchomi konkretny plik, mimo że nie zaczyna się od test*.

`pytest -v .\ksiazka_py\testy15\py_17flatten_pytest.py` 
Jeśli w folerze testy15 jest `__init__.py`
to pytest się wywali w porównaniu do python -m pytest.

`python -m pytest -k daj -v`
Uruchomi wszystkie testy mające w nazwie metody 'daj'.

`python -m pytest -m szczegolowe -W ignore::UserWarning -v`
Ukrywa warningi.

`@pytest.mark.szczegolowe`
Dekorator dodany nad metodami testującymi grupuje je do jednej nazwy.
Dodanie go powoduje ignorowanie normalnych nazw metod.
Po takim dodaniu podczas testów będą wyświetlane warningi, aby dodać 'szczegolowe' do przestrzeni mark.
Można to zrobić dodając plik pyproject.toml, a w opis nowych marks formacie z dokumentacji.

`python -m pytest ksiazka_py/testy15/testy21fixtury -v -s`
`-s` powoduje wyświetlenie out z konsoli print().

`def setup_module(): ... oraz def teardown_module():`
Uruchomi się na początku i na końcu pliku testów.

fixtura - metoda, która przygotowuje dane lub wykonuje czynności inicjalizacyjne na potrzeby testów.

`@pytest.fixture`
Dodanie tego dekoratora nad naszą customową metodę i wpisanie nazwy dekorowanej metody,
jako parametru w definicji wybranych testów spowoduje uruchomienie tej metody przed uruchomieniem każdego z tych testów.

`@pytest.fixture(scope='module')`
Dekorator nad naszą customową metodą spowoduje uruchomienie tej f.
jeden raz przed uruchomieniem testów z nazwą tej f. w definicji parametrów.

`@pytest.fixture(autouse=True)`
`autouse` zadziała tak tak `setup_module` - nie trzeba podawać nazwy funkcji w parametrach testów,
można mieszać ze scope='module', w tedy uruchomi się 1 raz dla całego modułu.

`python -m pytest --cov`
Sprawdzi cały projekt pod względem pokrycia kodu testami.

`python -m pytest --cov=ksiazka_py`
Pominie inne biblioteki i sprawdzi pokrycie tylko mojego kodu.

`python -m pytest ksiazka_py/testy15/testy20param/ --cov --cov-report=html`
Sprawdzić tylko wskazany folder, a wynik wrzuci to katalogu projektu do folderu htmlcov.

`pytest -W ignore::DeprecationWarning -s`
`-W ignore::...` nie pokazuje tego rodzaju warningów.

------------------
Fajne libki pomagające ogarniać kod:
- Flake8: Sprawdza poprawność pisowni ze standardem PEP8 i innymi standardowymi guidelineami.
- mypy: Analizuje typy danych w kodzie nie uruchamiając go. Potrafi wykryć potencjalne błędy.
- isort: Sprawdza poprawność sortowania importów z modułów w naszym kodzie
- black: Automatyczny linter który w jednoznaczy sposób wyznacza sposób pisowni, deterministyczny i bardzo przydatny w pracy zespołowej.

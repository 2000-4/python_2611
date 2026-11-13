# Python 학습 및 실습 프로젝트 정리

이 폴더(`/home/mcea/Documents/python`)는 파이썬 기초 문법부터 심화 개념, 데이터 분석 및 시각화 라이브러리(`NumPy`, `Pandas`, `Matplotlib`), 엑셀 자동화(`openpyxl`), 웹 스크래핑/크롤링(`BeautifulSoup`, `Selenium`)까지의 실습 예제를 담고 있습니다.

---

## 1. 디렉토리 구조

```text
python/
├── exam.py                # 파이썬 기초 문법 종합 실습 (조건문, 반복문, 함수, 자료구조, 클래스)
├── ex1.py                 # 사용자 정의 모듈 테스트용 파일
├── moduleEx.py            # 파이썬 표준 모듈(내장 라이브러리) 활용 예제
├── anno_ex.py             # 타입 어노테이션(Type Annotation) 예제
├── cl_de_ex.py            # 클로저(Closure)와 데코레이터(Decorator) 예제
├── unicode_ex.py          # 유니코드(ord, chr) 및 문자열 인코딩/디코딩 예제
├── re_ex.py               # 정규표현식(re 모듈) 기초 및 패턴 매칭 예제
├── test.xlsx              # openpyxl 기본 실습 결과 파일
├── bg_color.xlsx          # openpyxl 셀 배경색 적용 결과 파일
├── chart_exam.xlsx        # openpyxl 바 차트 생성 결과 파일
├── libs/                  # 데이터 분석 및 시각화 라이브러리 실습
│   ├── num.py             # NumPy 다차원 배열(ndarray) 및 수치 연산 실습
│   ├── pd.py              # Pandas DataFrame/Series 조작 및 결측치 처리 실습
│   └── mat.py             # Matplotlib 그래프 및 서브플롯 시각화 실습
├── openpyxl/              # 엑셀 파일 자동화(openpyxl) 실습
│   ├── openpy_exam.py     # 워크북 생성, 저장, 불러오기 및 셀/범위 값 입력
│   ├── openpy_exam2.py    # 새로운 시트 생성 및 시트 이름 변경
│   ├── openpy_exam3.py    # PatternFill을 활용한 셀 배경색 지정
│   ├── openpy_exam4.py    # BarChart, Reference를 활용한 엑셀 차트 생성
│   └── test.csv           # CSV 모듈 테스트용 파일
├── web/                   # 웹 기초 및 정적 웹 스크래핑 실습
│   ├── index.html         # HTML 태그 및 CSS 선택자(태그, class, id) 기초 예제
│   ├── style.css          # CSS 스타일시트 (빈 파일)
│   ├── script.js          # JavaScript 스크립트 (빈 파일)
│   ├── scrap_ex.py        # requests + BeautifulSoup 기본 HTML 파싱 예제
│   └── nv_scrap.py        # User-Agent 헤더 설정 및 네이버 뉴스 스크래핑 예제
└── selenium/              # 동적 웹 크롤링 및 브라우저 자동화(Selenium) 실습
    ├── sel_ex.py          # Chrome 드라이버 실행 및 기본 요소(CLASS_NAME) 탐색
    ├── sel_ex2.py         # 다양한 요소 탐색 방식 (TAG_NAME, CLASS_NAME, ID, XPath)
    ├── sel_ex3.py         # 단일 페이지 내 명언·저자·태그 구조화 수집
    └── sel_ex4.py         # 페이지네이션(Next 버튼 클릭)을 통한 다중 페이지 반복 크롤링
```

---

## 2. 루트 폴더: 파이썬 기초 및 심화 문법

### `exam.py` — 파이썬 기초 문법 종합
- **조건문 및 연산자**: 비교 연산자(`==`, `!=`, `>`, `>=`), 논리 연산자(`and`, `or`, `not`), `if-elif-else` 분기문
- **반복문**: `while` 및 `for ... in range()` 반복문, 중첩 반복문을 활용한 구구단 출력
- **함수**: 매개변수(Parameter)와 인자(Argument) 개념, 소수 판별 함수(`is_prime_number`) 작성
- **컬렉션 자료형**:
  - `list`: 원소 추가(`append`, `+=`), 수정(`index`), 검색(`in`), 삭제(`del`, `pop`, `remove`)
  - `dict`: 키-값 쌍 생성 및 반복문을 통한 월별 말일 데이터(`month_end_days`) 구성
- **문자열(String) 및 예외 처리**: 문자열 길이(`len`), 인덱싱/슬라이싱, 조건 필터링, `try-except ValueError` 예외 처리
- **객체지향 프로그래밍(OOP)**:
  - `class` 정의 및 인스턴스 생성, `self`의 역할, 생성자(`__init__`)
  - 비공개 속성(`__weight`, Private Attribute)과 클래스 공용 속성(`folder`)

### `ex1.py` & `moduleEx.py` — 모듈 활용
- **사용자 정의 모듈**: `ex1.py`에 정의된 `funA()`, `funB()`, `funC()`를 `import ex1` 또는 `from ex1 import funA`로 불러와 사용하는 방법 실습
- **파이썬 내장 모듈**:
  - `math`: 제곱근(`sqrt`), 거듭제곱(`pow`)
  - `random`: 난수 생성(`randint`)
  - `datetime` / `time`: 현재 시간 조회(`datetime.now()`) 및 실행 지연(`time.sleep()`)
  - `sys` / `os`: 파이썬 버전 확인(`sys.version`) 및 현재 작업 경로 확인(`os.getcwd()`)
  - `json`: 딕셔너리 데이터를 JSON 문자열로 변환(`json.dumps()`)
  - `re`: 정규표현식 매칭(`re.match()`)
  - `csv`: CSV 파일 쓰기(`csv.writer().writerow()`)
  - `collections.Counter`: 문자열 내 각 문자의 빈도수 계산

### `anno_ex.py` — 타입 어노테이션 (Type Annotation)
- 변수 타입 명시 (`age: int = 30`)
- 함수 매개변수 및 반환값 타입 힌트 (`def add(a: int, b: int) -> int:`)
- 컬렉션 타입 어노테이션 (`list[int]`, `dict[str, int]`) 및 동적 타이핑 주의사항

### `cl_de_ex.py` — 클로저와 데코레이터
- **중첩 함수와 일급 객체**: 함수 내부에 함수를 정의하고 함수 자체를 반환(`return inner`)
- **클로저(Closure)**: 외부 함수(`make_multiplier(x)`)의 지역 변수를 내부 함수(`multiplier(n)`)가 기억하여 활용하는 구조
- **데코레이터(Decorator)**: `@decorator` 문법을 사용해 기존 함수 수정 없이 실행 전후 동작을 감싸는(`wrapper`) 구조 및 인자가 있는 함수 데코레이팅(`decorator_width_args`)

### `unicode_ex.py` — 유니코드 및 인코딩/디코딩
- 문자와 유니코드 코드 포인트 변환 (`ord('가')` ↔ `chr(44032)`)
- `encode('utf-8')`를 통한 바이트(`bytes`) 변환과 `decode('utf-8')`를 통한 문자열 복원
- 인코딩 방식 불일치(`cp949`) 시 발생하는 `UnicodeDecodeError` 예외 처리

### `re_ex.py` — 정규표현식 (`re` 모듈)
- 기본 메타문자 및 수량자: `\d` (숫자), `\w` (문자/숫자), `[a-z]`, `+` (1개 이상), `*` (0개 이상), `?` (0 또는 1개)
- 이메일 패턴 추출 예제 (`r'\w+@+\w+.\w+'`)
- 주요 함수 실습: `re.findall()`, `re.search().group()`, `re.sub()` (문자열 치환)
- 크롤링 데이터 정제 활용법 (숫자만 추출, 단위 제거, 특정 형식 탐색)

---

## 3. `libs/` 폴더: 데이터 분석 및 시각화 라이브러리

### `libs/num.py` — NumPy 다차원 배열 실습
- **배열 생성 및 연산**: `np.array()`를 이용한 1·2·3차원 `ndarray` 생성 및 브로드캐스팅 사칙연산
- **배열 속성 확인**: `ndim` (차원 수), `shape` (구조 튜플), `size` (전체 원소 수), `dtype` (데이터 타입), `itemsize` (메모리 바이트 크기)
- **형태 변환**: 전치 행렬(`arr.T`), 1차원 평탄화(`arr.flatten()`), 차원 재구성(`arr.reshape(2, 3)`)
- **집계 함수 및 축(`axis`) 연산**: `sum()`, `mean()`, `min()`, `max()`를 전체, 열 방향(`axis=0`), 행 방향(`axis=1`)으로 계산
- **초기화 함수**: `np.zeros()`, `np.ones()`, `np.full()` 및 기존 배열의 형태를 본뜨는 `*_like` 계열(`zeros_like`, `ones_like`, `full_like`)
- **난수 생성**: `np.random.randint()`와 시드 고정(`np.random.seed()`)
- **인덱싱과 슬라이싱**: 다차원 인덱싱(`arr2[0, 1]`), 슬라이싱(`arr2[1:2, 1:3]`), Fancy 인덱싱(`arr1[[0, 1, 3]]`)

### `libs/pd.py` — Pandas 데이터프레임 실습
- **자료구조 생성**: 2차원 표 형태의 `pd.DataFrame` 및 1차원 열 데이터인 `pd.Series` 생성
- **통계 및 구조 요약**: `max`, `min`, `mean` 확인, 요약 통계량(`df.describe()`), 데이터프레임 메타 정보(`df.info()`)
- **데이터 선택 및 조회**:
  - 위치 기반 인덱싱(`df.iloc[]`) vs 라벨 기반 인덱싱(`df.loc[]`)
  - 상위/하위 행 확인 (`df.head()`, `df.tail()`)
- **열 조작**: 새 열 추가(`df['Survived'] = ...`), 열 이름 변경(`df.rename()`), 열 삭제(`df.drop(..., axis=1)`)
- **결측치(NaN) 처리**: 결측치 확인(`isnull()`), 결측치 행 제거(`dropna()`), 특정 값으로 대체(`fillna()`), 앞/뒤 행 값으로 채우기(`ffill()`, `bfill()`)

### `libs/mat.py` — Matplotlib 데이터 시각화 실습
- **기본 플롯 및 서브플롯**: `plt.figure()`와 `fig.add_subplot(행, 열, 위치)`을 활용한 영역 분할
- **스타일 및 마커 지정**: `plt.style.use('default' / 'ggplot')`, 마커 및 색상 포맷 지정(`'yD'`, `'m*'`)
- **막대 그래프**: 세로 막대(`a.bar()`) 및 가로 막대(`a.barh()`)에 라벨(`tick_label`)과 색상(`color`) 적용

---

## 4. `openpyxl/` 폴더: 엑셀 자동화

| 파일명 | 생성/대상 엑셀 파일 | 주요 실습 내용 |
| :--- | :--- | :--- |
| `openpy_exam.py` | `test.xlsx` | `Workbook()`으로 새 엑셀 생성 및 저장, `load_workbook()`으로 불러오기, 단일 셀(`ws['A1']`) 및 범위(`ws['D5':'F8']`)에 반복문으로 값 입력 |
| `openpy_exam2.py` | `test.xlsx` | `create_sheet()`로 새 워크시트 추가 및 `title` 속성으로 시트 이름(`'마지막_시트'`) 변경 |
| `openpy_exam3.py` | `bg_color.xlsx` | 1행에 과목 헤더 입력 후 `PatternFill(fill_type='solid', fgColor='b2e018')`로 헤더 행 전체 배경색 지정 |
| `openpy_exam4.py` | `chart_exam.xlsx` | `ws.append()`로 학생 점수 데이터 추가 후 `BarChart()`와 `Reference()`를 사용해 막대 차트를 생성하고 `E5` 셀 위치에 삽입 |
| `test.csv` | - | `name,score` 헤더가 기록된 CSV 테스트 파일 |

---

## 5. `web/` 및 `selenium/` 폴더: 웹 기초 및 크롤링

### `web/` — HTML 기초 및 정적 웹 스크래핑 (`requests` + `BeautifulSoup`)
- **`index.html`**: HTML 기본 구조(`h1`, `p`, `a`, `div`)와 CSS 선택자(태그, `.class`, `#id`) 개념 설명 및 스타일 적용 예제 (`style.css`, `script.js`는 빈 파일)
- **`scrap_ex.py`**:
  - `requests.get()`을 통한 웹 요청 및 HTTP 상태 코드(200, 301/302, 403, 404, 500) 정리
  - `BeautifulSoup(html_doc, 'html.parser')`와 `soup.select('a')`를 이용해 텍스트(`.text`)와 속성(`['href']`) 추출
- **`nv_scrap.py`**:
  - `User-Agent` 헤더를 설정하여 `https://news.naver.com` 요청 후 `.cnf_news_item` 클래스 요소를 선택해 뉴스 텍스트 출력

### `selenium/` — 동적 웹 크롤링 (`Selenium WebDriver`)
대상 사이트: [https://quotes.toscrape.com/](https://quotes.toscrape.com/)
- **`sel_ex.py`**: `webdriver.Chrome()`으로 브라우저 실행, `find_element`와 `find_elements`(`By.CLASS_NAME, 'text'`)로 명언 텍스트 수집 후 `driver.quit()` 종료
- **`sel_ex2.py`**: 요소 탐색 방법 비교
  - `By.TAG_NAME`, `By.CLASS_NAME`, `By.ID`
  - `By.XPATH`: 상대 경로(`//div[@class='quote']/span[@class='text']`) 및 인덱스(`(//div[@class='quote'])[1]`)를 이용한 계층 탐색
- **`sel_ex3.py`**: 한 페이지 내 모든 `.quote` 블록을 순회하며 명언(`text`), 저자(`author`), 태그 리스트(리스트 컴프리헨션 활용)를 딕셔너리 리스트(`results`)로 구조화하여 수집
- **`sel_ex4.py`**: `MAX_PAGES = 3` 제한을 두고 `By.CSS_SELECTOR` (`'li.next a'`)로 다음 페이지 버튼을 찾아 클릭(`.click()`)하며 여러 페이지의 명언 데이터를 연속 크롤링

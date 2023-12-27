# 소프트웨어 분석 연구실 홈페이지 수정하기
소프트웨어 분석 연구실 홈페이지는 [Hugo](https://gohugo.io/)를 이용하여 만들어졌습니다.
Hugo는 정적 웹사이트 생성기로, 마크다운 문법을 이용하여 웹사이트를 만들 수 있습니다.
이 문서는 소프트웨어 분석 연구실 홈페이지를 수정하는 방법을 설명합니다.

## Hugo 설치하기
이 저장소는 Github Actions를 이용하여 자동으로 빌드되어 배포되고 있습니다.
따라서, 로컬에 Hugo를 설치하지 않고 수정하고 Github에 푸시하면 자동으로 배포됩니다.
하지만, 배포되기까지 시간이 걸리기 때문에 로컬에서 수정하고 확인하고 싶다면 Hugo를 설치해야 합니다.
Hugo는 [Homebrew](https://brew.sh)를 이용하여 설치할 수 있습니다:
```bash
brew install hugo
```

Hugo를 설치한 후에는 아래의 커맨드로 로컬에서 웹사이트를 확인할 수 있습니다:
```bash
hugo server -D
# https://localhost:1313 에서 확인 가능
```

## 페이지 수정하기
홈페이지의 내용은 `content` 디렉토리에 마크다운 파일로 저장되어 있고, 폴더 구조가 그대로 웹사이트의 URL이 됩니다.
예를 들어, `content/about/_index.md` 파일은 `https://kupl.github.io/about/`에 해당하는 페이지를 만듭니다.

Hugo의 마크다운 파일은 아래와 같은 형식을 가지고 있습니다:
```markdown
+++
draft = false
title = '<Your Title>'
# other metadata in TOML format
+++

<!-- Contents to display -->
``````

`+++` 사이에는 [TOML](https://toml.io/) 형식으로 작성된 페이지의 메타데이터가 들어갑니다.
빌드되는 모든 페이지는 아래와 같은 두 변수를 설정할 수 있습니다:
| 변수 | 설명 |
| --- | --- |
| `draft` | `true`로 설정하면 배표용 빌드에 포함되지 않음 |
| `title` | 페이지의 제목(브라우저의 탭에 표시되는 내용) |

위의 두 변수 이외에도 각 페이지 별로 다른 변수를 지원하는데, 자세한 내용은 이후에 각 페이지를 설명할 때 다루겠습니다.

메타데이터를 작성한 후에는 페이지의 내용은 마크다운 형식으로 작성하면 됩니다.
기본적인 마크다운의 문법은 [여기](https://www.markdownguide.org/basic-syntax/)를 참고하시면 됩니다.

### 메인 페이지
메인 페이지는 `content/_index.md` 파일을 랜더링하지 않고, `layouts/index.html` 파일을 직접 렌더링합니다.
현재는 `content/about/_index.md` 파일과 완전히 동일하게 랜더링하도록 되어 있습니다.

### Members
연구실의 구성원을 보여주는 페이지입니다.
각 구성원은 본인의 정보를 `content/members/<your-name>/` 아래와 같은 구조로 구성하면 됩니다:
```text
content/members/<your-name>/
├── index.md
├── portrait.png
├── cv.pdf
└── ...
```

구성원 페이지의 메타데이터는 아래와 같은 변수를 지원합니다:
| 변수 | 설명 |
| --- | --- |
| `title` | 구성원의 이름 |
| `ko` | 구성원의 한글 이름 |
| `portrait` | 구성원의 사진 |
| `role` | 구성원의 직책 |
| `affiliation` | 구성원의 소속(복수 지정 가능) |
| `affiliation.name` | 소속의 이름 |
| `affiliation.url` | 소속의 URL |
| `materials` | 자료(표시 이름 = 자료) |

메타데이터의 구체적인 사용방법은 `content/members/hakjoo-oh/index.md`와 [여기](https://kupl.github.io/members/hakjoo-oh/)를 참고하시면 됩니다.

#### 링크 만들기
구성원 페이지를 생성한 후에는 `content/members/_index.md` 파일에 링크를 추가해야 합니다.
링크는 아래와 같이 추가하면 됩니다:
```markdown
- [Your Name]({{< relref "your-name" >}})
```

### Publications, Talks, Trips
Publications, Talks, Trips 페이지는 각각 `data/publications.yaml`, `data/talks.yaml`, `data/trips.yaml` 파일의 정보를 이용하여 랜더링합니다.
각 파일의 맨 위에 있는 주석을 참고하시어 데이터를 수정하시면 됩니다.

### Courses
연구실에서 진행했던 강의를 보여주는 페이지입니다.
각 강의는 `content/courses/<id>/<year>` 아래와 같은 구조로 구성하면 됩니다:
```text
content/courses/<id>/<year>/
├── _index.md
├── syllabus.pdf
├── slides
│   ├── lec1.pdf
│   ├── lec2.pdf
│   └── ...
└── ...
```

#### 링크 만들기
강의 페이지를 생성한 후에는 `content/courses/_index.md` 파일에 링크를 추가해야 합니다.
링크는 아래와 같이 추가하면 됩니다:
```markdown
- [New Course]({{< relref "course-id/year" >}})
```

## 코드 조각
마크다운을 작성하면서 활용할 수 있는 다양한 코드 조각들입니다.

### 링크
링크는 아래와 같이 작성하면 됩니다:
```markdown
[relative link](./relative/path)
[absolute link](/absolute/path)
[external link](https://example.com)
```
상대 경로는 현재 페이지를 기준으로, 절대 경로는 홈페이지(`https://kupl.github.io/`)를 기준으로 계산됩니다.

#### `ref`와 `relref`
`ref`와 `relref`는 Hugo의 내장 함수로, 각각 절대 경로와 상대 경로를 계산하여 반환합니다.
이때, 링크의 존재 여부를 컴파일 과정에서 검사해줍니다.
`ref`와 `relref`는 아래와 같이 작성하면 됩니다:
```markdown
[absolute link]({{< ref "/absolute/path" >}})
[relative link]({{< relref "relative/path" >}})
```


### 이미지
이미지는 아래와 같이 `figure` 코드 조각을 이용하여 삽입할 수 있습니다:
```markdown
{{< figure src="..." width="..." link="..." target="_blank" >}}
```
각 인자는 아래와 같은 의미를 가집니다:
| 인자 | 설명 |
| --- | --- |
| `src` | 이미지의 경로 |
| `width` | (Optional) 이미지의 너비 |
| `link` | (Optional) 이미지를 클릭했을 때 이동할 링크 |
| `target="_blank"` | (Optional) `link`를 주어졌을 때 새로운 창에서 열기 |

### HTML 코드 조각
HTML 코드 조각을 아래와 같이 `html-snippet` 코드 조각을 이용하여 직접 삽입할 수도 있습니다:
```markdown
{{< html-snippet >}}
<div class="fs-2 fw-bold text-center mb-3">
    <span class="text-primary">Software Analysis Laboratory</span>
</div>
{{< /html-snippet >}}
```

## 디자인
홈페이지는 [Bootstrap](https://getbootstrap.com/)을 이용하여 만들어졌습니다.
Hugo는 `layouts` 디렉토리에 있는 HTML 파일을 이용하여 웹사이트를 렌더링합니다.

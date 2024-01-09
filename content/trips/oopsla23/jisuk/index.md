+++
draft = false
title = 'SPLASH 2023 in Cascais, Portugal'
author = '변지석, 고려대학교 소프트웨어 분석 연구실'
from = '2023.10.23'
to = '2023.10.27'
autonumbering = true
+++

{{< figure src="splash-room.jpg" height=500 title="" alt="Conference room setup for the Splash event in Cascais 2023, with a large projector screen displaying the event's title and logos of sponsors like Huawei, Ahrefs, Prime Video, Google, and IBM. Red chairs with curved backs are neatly arranged in rows, facing the screen. A camera on a tripod stands to the left, ready to record, and a potted palm tree adds a touch of greenery to the right side of the room." >}}


# 들어가며
최고 수준의 프로그래밍 언어 학회들 중 하나인 OOPSLA 2023 (Object-Oriented Programming, Systems, Langauges & Applications) 에 참석했다. OOPSLA 는 SPLASH 학회의 일부인 형태로 열리며, 그 중 가장 큰 비중을 차지하고 있다. 연구실 찬구의 양자회로 합성 연구발표에 동행할 기회를 얻어 2023년 10월 23일부터 10월 27일까지 진행되는 학회 참석 일정을 연구실 사람들과 함께했다.

지난 2022년 POPL 과 이번 OOPSLA 에서의 경험을 비교해 보았을 때, OOPSLA 에서 발표되는 연구들에는 내가 가진 배경지식으로 들을 수 있는 연구들이 조금 더 많았던 것 같다.

이 보고서를 통해 학회에서 경험하고 생각했던 내용들과 인상깊게 들었던 발표들, 그리고 학회장소 포르투갈과 경유지 핀란드에서 느낀 점들을 공유하고자 한다.


{{< figure src="conference-venue.jpg" height=500 title="컨퍼런스 개최 장소인 호텔 카스카이스 미라젬 입구. 학회 장소에서 사진 2층 유리창을 통해 바깥을 내다볼 수 있었다. 사진 속 인물은 학회 첫날 아침의 도원, 하영, 미령, 그리고 찬구." alt="Entrance of a modern conference venue with a high ceiling supported by square columns. People are scattered around the space, some walking and others standing in groups, chatting. A man in a white shirt and black trousers walks across the foreground, while a car is parked by the curb, and the interior of the building is visible through the glass facade in the background." >}}

# SPLASH 2023

## 학회 장소
SPLASH 2023 이 열리는 카스카이스는 유럽의 서남쪽 끄트머리 포르투갈에서도 서쪽에 위치한 해안도시로, 항구도시로서의 산업 요충지나 넓은 자연환경을 내세우기보다는 멋진 해수욕장과 즐길거리를 강조하는 모습의 관광도시였다.

학회 장소 또한 남쪽으로 유리벽과 문을 내놓은 호텔 미라젬 2층에서 이뤄졌는데, 2층은 넓은 1층 로비를 내려다볼 있게 가운데다가 크고 네모나게 바닥을 뚫어놓았고, 서쪽 변에 층을 오가는 계단을 변에 평행하게 놓아두었다. 큰 구멍이 있음에도 학회가 진행되는 2층은 넓어서 쉬는 시간에 많은 사람들이 세션 진행 방 밖으로 나와있는데 그 사이를 지나다니는 것이 그리 불편하지 않았다.

네모난 동선의 서쪽 변을 제외한 삼면에서 점심식사와 다과, 음료를 제공해주었다. 학회 참석 첫날 수준 높은 식음료와 다과에 매우 만족했었는데, 둘째날에도 완전히 같은 구성으로 제공되어 그 밋밋함에는 조금 실망했다. 나눠주는 그릇에 동그란 구멍이 있는 플라스틱 조각을 끼워주길래 엄지손가락을 끼워 접시 윗면에 손이 안닿게 도와주는 도구인가 싶어 엄지손가락을 끼워 들고 다녔는데, 음료 잔의 목 부분을 끼워 사용하는 도구인 것을 나중에 알아서 이후에 엄지손가락을 넣고 다니는 짓은 하지 않았다.

OOPSLA 학회 발표의 많은 수가 서쪽 변에 맞붙은 Room1, Room2 에서 진행되었는데, Room1 의 경우 두꺼운 커튼으로 남쪽 유리벽 너머 아름다운 바다와 밝은 햇빛을 막아두지 않았다면 바깥에 정신이 팔려 발표를 제대로 듣지 못했을 것이다.

## 기계학습 & 인공지능
OOPSLA 에서도 기계학습과 인공지능은 주요 토픽 중 하나였다. 크게 기계학습/AI 모델을 활용해서 문제를 푸는 경우와 기계학습/AI 시스템을 프로그래밍 대상으로 보았을 때의 문제점 제시 두 경우의 연구가 주로 등장했고, Code LLM (Large Language Model) 의 사용목적을 정리한 스터디 연구가 독특하게 하나 발표되었다.

1. **Scaling Machine Learning without Tears**
    첫날 키노트는 모델의 학습과 추론계산을 위한 기계학습 시스템을 설계할 때 수반되는 문제점들에 대해 구글 딥마인드에서 연구한 내용들을 소개하는 자리였다. 병렬처리 및 스케쥴링을 표현하는 고수준 인터페이스 및 컴파일러를 새로 만드는 것으로 네 문제를 풀었다고 소개했다: i) 병렬처리 및 스케쥴링 표현 인터페이스 제공 ii) 더 빠른 연산전략을 컴파일러 옵션으로 쉽게 적용 iii) 고수준으로 적힌 모델 시뮬레이션 iv) 모델 자동 최적화.

    기계학습 시스템 표현 DSL 및 텐서 연산 컴파일 과정은 오늘날 각광받는 산업에 직접적으로 영향을 미칠 수 있다는 점에서 흥미로웠지만, 반대로 저 연구를 연구실에서만 한다면 정말 산업에 쓰일 수 있을지, 실험은 어떻게 해야 좋을지 엄청 고민될 것으로 보인다. 또, 이를 보며 PLDI'23 에서 소개된 Tensor Algebra 컴파일러 연구가 떠올랐는데, 이번 발표의 주 내용은 하드웨어들을 직접 다루는 시스템 설계를 위한 언어라는 점에서 Tensor Algebra 컴파일러와는 다르겠구나 싶었다.

1. **Grounded Copilot: How Programmers Interact with Code-Generating Models**
    사람들은 Code LLM 인 Copilot 을 통해 프로그래밍의 autocompletion(Acceleration) 과 answer-for-question(Exploration) 두가지를 원한다고 주장하는 연구였다. 메시지를 듣자마자 뭔가 “당연한거 아냐? 난 이미 그런 걸 원해서 사용하고 있어” 라는 느낌이 들었지만, 조사내용을 정돈된 발표로 듣는것은 굉장히 재밌었다. 발표에서는 피실험자들이 프로그래밍 과제를 Copilot 을 가지고 수행하는 모습 기록을 영상과 음성으로 보여줬는데, 한 피실험자가 Copilot 을 사용하면서 “Wow, I’m such a good coder” 라고 자축하는 모습을 보여줬을 때는 청중들이 모두 웃었다. 여태껏 User study 경험을 화면과 목소리 녹음으로 기록해두는 모습에 대해 전혀 생각하지 못했는데 매우 좋은 조사 방법인 것 같다.

    이를 들으며 현재 Code LLM 의 한계점이 먼저 떠올랐었다. LLM 은 자연어 처리를 우선으로 하기에 파싱된 Context (free/sensitive) 문법 형태의 코드 생성을 해내지 못했는데 이 때문에 잘못된 코드를 쉽게 만들어낸다. 오히려 그래프를 출력하도록 하는 모델이 있다면 코드의 Syntax/Semantic 구조를 표현하는 그래프를 출력하도록 시키고 이를 코드로 변환하는 것으로 코드를 합성해내는데 더 정교하고 치밀한 작업을 수행시킬 수 있을 것이라 상상했다.

    그리고 Code LLM 을 사용하는 프로그래밍 환경에서 새로 발생하는 문제점으로 i) 모델의 응답 때문에 오히려 새로운 작성방법 가능성을 탐색하느라 시간을 지체하는 경험 ii) 모델의 응답이 왜 정답인지 모름 iii) 다수의 모델 응답들이 어떻게 다른것인지 확인이 어려움 등을 들었는데, 오늘날 프로그래밍 환경 자체가 LLM 도움을 병행하도록 바뀌는 상황에서 제시된 문제를 풀어내고 프로그래밍을 돕는 목표는 영향력이 큰 연구가 될 것이라 생각한다.

1. **Turaco: Complexity-Guided Data Sampling for Training Neural Surrogates of Programs**
    주어진 프로그램에 대한 Neural Surrogate 모델이란 주어진 프로그램의 입출력을 잘 흉내내는 신경망 프로그램으로, 나는 이 날 Neural Surrogate 을 잘 만들겠다는 분야가 있다는 것을 처음 들어봤다. Computer Vision 에서 NeRF 같은 방법이 있다는걸 응용하면 프로그램의 입출력 행동에 대한 surrogate model 이 만들어질 수도 있다는 점을 진작에 눈치챘어야 했는데 말이다. 이 연구에서는 Neural Surrogate 를 잘 학습시키기 위해서는 학습데이터로 입출력 쌍을 잘 만들어줘야 한다고 주장하며, 여기서 입력 Sampling 을 잘 하는 방법을 새로 제안한다고 하며, 이로서 학습시킨 모델의 정확도를 높일 수 있었다고 한다. 아직 Surrogate Model 입출력 데이터 타입이 매우 제한적이라 추측되는데, 그 범위를 더 넓히는 것도 멋진 연구가 될 것 같고 이를 응용해서 복잡한 프로그램의 테스트 실행시간을 단축시킬 수 있지 않을까 싶기도 했다.

1. **Concrete Type Inference for Code Optimization using Machine Learning with SMT Solving**
    ML & SMT 를 이용한 파이썬 타입 추론이라고 해서 모든 객체의 타입을 제대로 추론할 수 있을까 기대했지만 추론하는 타입의 범주가 함수, 정수 등의 적은 수의 primitive type과 기계학습에서 주로 쓰이는 Array, Matrix 타입들 뿐이라 조금 실망스러웠다. 다만 저자들이 이토록 파이썬 타입 추론의 범주를 줄인 결정은 합리적이라 생각하는데, 워낙에 파이썬 객체 타입 추론이 잘 정의되지 않았고, Tensor 크기/타입 추론만으로 문제의 범위를 줄여도 이를 통해 최적화에 도움이 된다는 점을 실험으로 보였으니 이정도만 해도 나쁘지 않다고 생각한다.

1. **Data Extraction via Semantic Regular Expression Synthesis**
    의미적 제약조건을 담은 정규표현식 합성이라는 새로운 문제를 제시하고 이를 풀어낸 흥미로운 연구였다. 정규표현식은 매우 잘 정의된 문법이고, 주어진 문자열을 표현할 수 있는 정규표현식 문법을 합성하는 문제는 전부터 풀어왔지만, 이 연구에서 제시한 문제는 기존 형식언어에서 전혀 다루지 않던 의미적 제약조건(사람 이름 문자열의 집합, 도시 이름 문자열의 집합 등)을 추가한 문법의 정의방법이 주어졌을 때 주어진 문자열을 표현할 수 있는 문법을 합성해내는 문제였다. 이와 같은 인간 사회의 지식과 관련된 문제를 새롭게 정의했기에 이 연구는 자연스럽게 LLM 을 도입시킬 수 있었다.

## 확률
나는 probabilistic programming 의 주 연구방향은 프로그램과 출력값 관찰로부터 입력 값의 분포/조건부확률 등을 직접 추론해내는 무시무시한 작업이라는 편견을 가지고 있었는데, OOPSLA probabilistic 세션에서 발표된 연구들은 예상과 달리 nondeterminism 을 확률적으로 표현하는 경우를 다루고 있어서 미리 겁먹었던것 보다는 잘 이해할 수 있었던 것 같다.

1. **A Deductive Verification Infrastructure for Probabilistic Programs**
    probabilistic choice 를 가진 프로그램을 대상으로 검증 도구를 만들었다고 소개하는 연구이다. 특정 값을 가질 확률, 프로그램이 끝날때에서의 기댓값, 그리고 프로그램 실행이 끝날 확률 등의 성질을 검증하는 것을 목표로 한다는데, 이를 자동화하기보다는 중간검증언어(IVL, intermediate verification language)을 정의하고 검증조건을 표현할 수 있도록 원리에 따른 도구를 제시하는 느낌이었다. 이 도구가 검증을 수행하기 위해 이용한 방법은 잘 알려진 검증방법인 가장약한-전조건 구하기와 비슷한 스타일의 가장약한-전기댓값(weakest preexpectation)으로, 계산된 가장약한-전기댓값이 주어진 전기댓값을 포함하고 있으면 검증이 된 것으로 여긴다. 전에 접하지 못했던 프로그램과 확률표현 사이의 대응에 대해 접할 수 있는 점은 좋았지만, 이 도구로 실제 어떤 검증 문제를 푸는데 도움이 되었는지 설명되지 않아 아쉬웠던 것 같다.

1. **A Gradual Probabilistic Lambda Calculus**
    파이썬과 같이 Gradual Typing 이 필요한 상황에서 데이터 타입 표현에 등장 확률(분포)을 병기할 수 있는 타입 시스템을 형식화한 연구이다. 예를 들어 함수의 반환값이 bool 타입일 확률을 0.9로, 이외에 에러가 날 확률을 0.1 이라고 표현하는 것이다. 이렇게 algebraic data type 이나 set theoretic type 으로는 표현되지 않는 성질을 타입으로 표현하는 것은 멋진 확장이라고 생각한다. 하지만 이러한 확률 타입을 gradual typing 조건에서 풀도록 시스템을 설계했다는 점이 석연찮다. 확률 타입 추론/체크에 static typing 을 쓰기 어려운 이유로 if-then-else 구문의 두 branch 에서 다른 확률 타입이 등장하면 static type checker 가 이를 거절할 것이라 소개했는데, 오히려 이 예제는 정확한 타입을 명시하거나 추론하기 어려운 이유로 보이고, 반대로 static type checker 가 소개된 대로 동작할 것으로 단정짓는 것이 이상한 것 같았다.

## 타입 시스템
OOPSLA 타입 시스템 세션에 발표되었던 연구의 절반 가량이 메모리 자원 관리와 관련된 내용이었는데, 원래 자원 관리를 타입시스템으로 해결하려는 것이 주요 연구 방향 중 하나였는지 아니면 새로운 동향인지 의문이 들었다.

1. **Reference Capabilities for Flexible Memory Management**
    Rust 언어 시스템이 실행시간에 쓰레기 수집기를 실행시키지 않고도 안전한 메모리 관리 방법을 제공하는 것과 비슷하게, 이 연구에서는 타입 시스템으로 안전한 메모리 관리 방법을 돕는 새 메모리 관리 시스템 Reggio 를 제안한다. Reggio 는 분산 시스템 설계용 언어 Verona를 위한 메모리 관리 시스템으로, Verona 가 힙 메모리 조각들을 영역(Region) 단위로 나눠들고 있는 상황을 반영해 영역 단위의 읽기/쓰기 (mutability) 권한을 추론하는 식으로 프로그램이 잘못된 메모리 사용을 하지 않도록 미리 체크해준다. 종종 메모리 영역을 여럿 나눌 수 있게 해주어 각 부분마다 다른 메모리 관리 방법을 적용한다면 좋지 않을까 상상해보곤 했는데, 목표점이 조금 다르지만 메모리가 영역별로 나뉘어 사용될 때 안전한 메모리 사용을 보장하게끔 하는 기술 연구를 듣게 되어 흥미로웠다.

1. **A Grounded Conceptual Model for Ownership Types in Rust**
    시스템 프로그래밍 배경지식이 없는 사람들이 Rust 공부하는 데 가장 어려워하는 것이 소유권(ownership) 개념이고, 이를 더 쉽게 교육시켜주고자 하는 연구이다. 더 잘 교육시키기 위해 인터넷 질문으로부터 초보자들이 어느 정도로 개념을 이해하고 있는지 조사하고, 현재 이해도와 실제 메모리 제약조건 사이의 중간 수준의 서술 방식과 그 서술 방식의 추론 방법을 설계했다. 그리고 새롭게 만든 서술방법으로 그린 도식을 잘 알려진 Rust 책 Rust programming book 에 병기한 버전을 새롭게 보였다 (https://rust-book.cs.brown.edu). Rust 의 ownership 이 이해하기 어렵다는 잘 알려진 사실을 바탕으로 사람들이 왜 어려워하는지 user study 를 진행하고, 어려움을 줄이기 위해 직접 자료를 만들었다는 점이 인상깊었다. 교육과 관련된 연구는 평가 실험이 어렵지만 실제 적용에 가장 빠르게 적용될 수 있는 분야 중 하나여서 멋져 보인다.

# 여정

## 비행기에서의 독서
우선 비행기에서의 도원의 독서 습관에 감탄을 금치 못했음을 밝힌다. 이번에 비행기 티켓을 같이 예매하게 되어 계속 옆자리에 앉을 수 있었는데, 도원이가 비행기 탑승 시간의 대부분을 독서로 보내는 모습을 옆에서 지켜볼 수 있었다. 또 그의 독서가 느린 것도 아니라서 가방 안에 읽을 책을 다 담지 못해 올 때 비행기에서 읽을 책은 캐리어에 따로 담아갈 정도였다. 송도원의 여행 보고서가 잘 읽히는 이유엔 그의 풍부한 독서가 한몫 할 것이다.

{{< figure src="airbnb-view.jpg" height=300 title="숙소의 멋진 전망. 학회 마지막날 아침" alt="Morning view from a high-rise building's corner window seat, with the sun rising above a coastal cityscape. Sunlight streams through the clouds, casting a soft glow over the sea and illuminating the city. The calm ocean extends to the horizon under a sky graced with the early light of day." >}}

{{< figure src="belem-tower.jpg" height=300 title="벨렝 탑" alt="Belem Tower standing majestically under a clear blue sky, its intricate limestone carvings and sturdy battlements highlighted by the bright sunlight. The Tagus River surrounds the tower, with gentle waves lapping against the stone embankment in the foreground." >}}

## 붉은 색 지붕
유럽은 어렸을 때 부모님과 짧게 여행한 이후 처음이었고, 그래서 숙소에서 포르투갈 집들의 붉은 지붕을 처음 접했을 때 이것이 포르투갈의 문화인 줄 착각했었다. 하지만 리스본 상조르즈 성에 올라 본 리스본 북부는 현대적인 건물들이 여럿 들어서 있었고, 붉은 지붕은 유럽 다른 나라에서도 쉽게 찾을 수 있는 그런 경험이라고 한다.

## 포르투갈에서 느낀 문화
포르투갈만의 눈에 띄는 특징을 찾아내기에 학회 전후로 둘러볼 시간과 내 지식이 짧았지만, 온화한 날씨, 유럽 문화, 그리고 해상 강국의 세가지 인상을 크게 받았었다. 체스 기물에서만 보던 유럽 성곽의 모양을 상조르즈 성에서 처음 만져볼 수 있었고, 온화한 날씨 덕에 카스카이스 파인애플처럼 머리가 난 나무를 볼 수 있었다. 페나 궁전에 전시된 일본 문화의 물건들과 중구난방으로 갖춰진 예술품들, 그리고 유명 관광지인 벨렝탑 동쪽의 리스본 발견기념비에 새겨진 위대한 항해자들의 조각을 통해 포르투갈이 한때 무역과 항해를 얼마나 활발히, 또 얼마나 중요시 여겼는지를 간접적으로 알 수 있었다.

그 외에 독특하다고 느낀 것은 다름아닌 참을성 하나 없는 운전문화였다. 처음에는 숙소로 가는 우버택시만 빠르게 운전하고 싶어하는 줄로만 알았는데, 골목길에서도 속도를 전혀 줄이지 않는 다른 차들과 성급하게 운전하다 인도 연석을 밟고 지나가는 택시 등을 겪다보니 이건 포르투갈에서 흔히 볼 수 있는 독특한 운전문화이겠거니 싶었다.

{{< figure src="temppeliaukion-church.jpg" height=300 title="헬싱키의 암석 교회 내부에서. 사진 속 인물은 도원과 나. 석현이 뒤에서 촬영해주었다." alt="Interior of Temppeliaukio Church in Finland, featuring visitors seated on wooden benches. The church's unique architecture is showcased with a sweeping copper ceiling adorned with small lights and rugged natural rock walls. The atmosphere is serene, with natural light filtering in, enhancing the tranquility of this rock-hewn space." >}}

## 헬싱키의 멋
우리가 비행기표를 예매할 때 포르투갈까지 가는 경유지를 어디로 할 지 적지 않게 고민했었는데, 헬싱키를 경유지로 고른 것은 숙소 위치, 음식점 선정과 더불어 이번 여정 최고의 선택이었다. 비록 한국보다 두어달은 빠른 추위에 떨었지만, 다소 차분한 도시 분위기와 깨끗한 자연이 편하게 느껴졌다.
헬싱키에서 멋진 자연과 차분한 도시, 그리고 몇 종교시설의 멋을 살펴볼 수 있었는데 그 중 현대 건축의 멋을 지닌 암석 교회에서는 도원이가 하나님께 기도를 드리자고 부추킨 덕에 기도하면서 인생이 가져야할 성질에 대해 생각해 볼 수 있었다.

# 마치며
연구를 제대로 마치지 못한 채 다른 분들 학회 참석에 자주 따라가는 것이 참으로 부담스러우면서도, 막상 참석할 때마다 학교에서 얻지 못하는 값진 배움과 경험을 얻을 수 있는 것이 이 감정을 어떻게 표현해야 할지 감이 잘 오지 않는다. 아마 더 많은 경험을 가진 만큼 더 열심히 연구해내는 것으로 풀어야 할 것 같다. 학회에서 멋진 발표를 마친 찬구와 지금까지 많은 기회를 주신 교수님께 감사를 전한다.
출장에 함께한 연구실 일원들, 도원, 석현, 하영, 미령에게 감사를 전하고, 그리고 찬구에게도 다시한번 감사를 전한다. 모두의 도움과 배려 덕에 많은 점에서 부족한 내가 무사히 다녀오는 것을 넘어 뜻깊은 경험을 얻어 돌아올 수 있었다.
마지막으로 이 보고서를 pdf가 아닌 웹페이지로 전달하려는 돌발적인 시도를 도와준 이석현에게 다시 한 번 감사를 전한다. 비록 기존의 보고서와 차별점을 보이는 색다른 시도를 하지는 못했지만, 앞으로 동영상을 띄우거나 모두가 함께 모여 하나의 웹페이지로서 보고서를 만드는 색다른 시도를 계획해볼 수 있을 것으로 기대한다.

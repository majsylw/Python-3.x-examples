# Metody numeryczne

Metody numeryczne są dziedziną, która zajmuje się metodami rozwiązywania problemów i zagadnień inżynierskich, matematycznych, ekonomicznych, fizycznych, i wielu innych na maszynach cyfrowych. Symulacje numeryczne pozwalają na rozwiązywanie dokładnych równań z kontrolowalną dokładnością, często ich wykonanie jest tańsze i szybsze niż przeprowadzenie badań doświadczalnych. Symulacje komputerowe pozwalają prześledzić wyniki dla praktycznie dowolnej funkcji i dowolnych parametrów – podają pełną informację o możliwych do osiągnięcia wynikach (lub pozwalają przewidzieć pewne niespodziewane efekty).

## Metoda Eulera - różniczkowanie numeryczne

Większości z rozwiązywanych zagadnień (równań różniczkowych) nie da się rozwiązać w sposób analityczny (to znaczy podać rozwiązania w postaci jawnej). W szczególności, największe problemy sprawiają równania zawierające człony nieliniowe. Świat, w którym żyjemy, jest silnie nieliniowy i większość problemów, które przyjdzie nam rozwiązywać, nie będzie posiadać rozwiązania w formie analitycznej. Metoda Eulera to sposób rozwiązywania równań różniczkowych, opierający się na interpretacji geometrycznej równania różniczkowego. W celu rozwiązania zagadnienia zastosujmy następujący schemat iteracyjny:<br>
𝑡<sub>𝑖+1</sub> = 𝑡<sub>𝑖</sub> + ℎ,<br>
𝑦<sub>𝑖+1</sub> = 𝑦<sub>𝑖</sub> + ℎ ∗ 𝑓(𝑡<sub>𝑖</sub>,𝑦<sub>𝑖</sub>),<br>
gdzie h jest krokiem całkowania, y<sub>𝑖+1</sub> szukanym rozwiązaniem, y<sub>𝑖</sub> rozwiązaniem dla wcześniejszego kroku, a f to funkcja obliczająca prawą stronę równania różniczkowego, tzn. 𝑓(𝑡,𝑦)=𝑑𝑦/𝑑𝑡.

Najprostszym przykładem zagadnieniem opisywanym za pomocą równania rózniczkowego jest zanik promieniotwórczy, którego przykład rozwiązania znajduje się w danym folderze (zadanie 2 z listy dodatkowej 3).

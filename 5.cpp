#include <iostream>
using namespace std;
int main () {
    double a1, a2, n; double temp = 0;  //инициализация
    cout << "Vvedite 1 chlen posledovatelnosti \n";
    cout << "a1 = "; cin >> a1;  //первый член последовательности
    cout << "Vvedite 2 chlen posledovatelnosti \n";
    cout << "a2 = "; cin >> a2;  //второй член последовательности
    cout << "Vvedite kolichestvo chlenov progressii \n";
    cout << "n = "; cin >> n; //количество членой прогрессии
    cout << "a1 = " << a1 << "\n";
    cout << "a2 = " << a2 << "\n";
    for (int i = 3; i<=n; i++) {  //вычисление i-ого члена програссии
        temp = a2; //сохранение a2 в временную переменную temp, чтобы посчитать значение следующего члена, 
                   //а затем значение a2 передать в a1
        a2 = 1.0/3*(a2/2 + a1/3);  // непосредственно вычисление i-го члена прогрессии
        cout << "a" << i << " = " << a2 << "\n"; //вывод нового члена прогрессии2
        a1 = temp;  //изменение значения нового предпоследнего члена на старый последний член
    }
    return 0;
}
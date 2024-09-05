/**
 * Funkcja dzielenia jedna liczba przez druga z wyjatkiem zera
 * @param a Pierwsza liczba
 * @param b Druga liczba
 * @returns {number} Wynik dzielenia a przez b
 * @example
 * a = 10;
 * b = 10;
 * return divide(a, b);
 * @throws {Error} błąd, gdy mianownik jest równy zero
 * @author Dawid Matelski 5D
 */

function divide(a, b) {
    if(b === 0) throw Error("divideBy0Exception");
    else return a / b;
}
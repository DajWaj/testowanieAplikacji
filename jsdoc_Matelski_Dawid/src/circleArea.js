/**
 * Funkcja obliczajaca pole kola
 * @param radius promien kola
 * @returns
 */

function calculateArea(radius) {
    if(radius <= 0) throw Error("radius <= 0");
    else circleArea = Math.pow(Math.PI, radius);
}
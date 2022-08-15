function formatinch(x) {
  return (
    Number.parseFloat(x).toFixed(2) + '" / ' +
    Number.parseFloat(x * 2.54).toFixed(2) + " cm"
  );
}

function calcwidthheight(diag, widthrat, heightrat) {
  breitediagverh = Math.sqrt(
    Math.pow(widthrat, 2) / (Math.pow(widthrat, 2) + Math.pow(heightrat, 2))
  );
  breite = diag * breitediagverh;
  hoehe = (breite / widthrat) * heightrat;

  return { width: breite, height: hoehe };
}

function printresults(diagonale,breitenverh,hoehenverh) {
    newresults = calcwidthheight(diagonale, breitenverh, hoehenverh);

    resultstext =
      "Diagonale: " + formatinch(diagonale) + '<br>\n' + 
      "Breite/Höhe: " + breitenverh + ":" + hoehenverh + '<br><br>\n\n' + 
      "Breite: " + formatinch(newresults.width) + '<br>\n' + 
      "Höhe: " + formatinch(newresults.height);

    let ergebnisse = document.querySelector(".ergebnisse");
    ergebnisse.innerHTML=resultstext;
}


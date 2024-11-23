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
      "<tr><td>" + formatinch(diagonale) + "</td>\n" + 
      "<td>" + breitenverh + ":" + hoehenverh + "</td>\n" + 
      "<td>" + formatinch(newresults.width) + "</td>\n" + 
      "<td>" + formatinch(newresults.height) + "</td></tr>\n";

    let ergebnisse = document.querySelector(".ergebnisse");
    ergebnisse.innerHTML=ergebnisse.innerHTML + resultstext;    
}



%sirina_polja = 3
%visina_polja = 3
%poskus = 'abcd'

% import model

    <h1> Križci in Krožci </h1>


    % if model.Igra.self.ali_je_zmagal_igralec():
    <h1> ZMAGAL SI! </h1>
    % elif model.Igra.self.ali_je_zmagal_racunalnik():
    <h1> IZGUBIL SI </h1>
    % else:
      %while not model.Igra.self.ali_je_zmagal_igralec() and not model.Igra.self.ali_je_zmagal_racunalnik():
        <table>
        %polje = 1
        % for st in range(visina_polja):
        <tr>
          % for st1 in range(sirina_polja):
              <td>
                <form action="/igra/"> 
                  % if polje not in model.zasedena_polja:
                    <button type = "submit" input type="hidden" name=polje>{{polje}}</button>
                    model.zasedena_polja.append(polje)
                  % else:
                    % if polje in model.igralceva_polja:
                        {{'X'}}
                    % else:
                        {{'O'}}
                    % end
                  % end
                </form>
              </td>
              %polje += 1
          % end
          </tr>
        % end
      % end
      </table>



    % end

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
$( document ).ready(function() {

      // console.log( "Neviim Jads...." );
      // jsonData.responseJSON.results["cpu_user"]     ==>   Como acessar os resultados do objeto de retorno.

      // Globalmente ativar plugins como cursor e marca-texto.
      $.jqplot.config.enablePlugins = true;
      // para 2 dígito bno ano, definir o padrão a 2000.
      $.jsDate.config.defaultCentury = 2000;



      var jsonData = $.ajax({ type: 'GET',
                                            url: 'http://localhost:4000/api/get_cpu',
                                            async: false,
                                            jsonpCallback: 'jsonCallback',
                                            dataType:"json",
                                            success: function(response){
                                                var trHTML = '';

                                                // não esto usando isso, no momento.
                                                $.each(response, function (i, item) {
                                                // trHTML += '<tr><td>' + item.rank + '</td><td>' + item.content + '</td><td>' + item.UID + '</td></tr>';
                                                  trHTML += '<tr><td>' + item.cpu_user + '</td><td>';
                                                });

                                                // parametro do html (#records_table)
                                                // <table id="records_table" border='1'>
                                                // <tr><th>Rank</th>
                                                //$('#records_table').append(trHTML);
                                            }
      });

      var cpu_user = [jsonData.responseJSON.results["cpu_user"]];

      // monta o grafico com os dados passados.
      $.jqplot('cpu_user',  cpu_user, {
          title: "Porcentagem de uso da CPU",
          highlighter: {show: true, sizeAdjust: 7.5},
          canvasOverlay:{
            show: true,
            objects: [
              {horizontalLine: {
                  y: 25,
                  lineWidth: 0.5,
                  color: 'rgb(255, 0, 0)',
                  shadow: false,
                  lineCap: 'butt'
              }},
              {dashedHorizontalLine: {
                  y: 13,
                  lineWidth: 0.5,
                  color: 'rgb(24, 116, 205)',
                  shadow: false,
                  dashPattern: [8, 16],
                  lineCap: 'round'
              }}
            ]
          },
          animate: true,
          animateReplot: true,
          cursor: {
              show: true,
              zoom: true,
              looseZoom: true,
              showTooltip: true
          },
          axes:{
              xaxis:{
                  label:'Dias - Hora:Minutos',
                  padMin: 0,
                  padMax: 1.2,
                  renderer:$.jqplot.DateAxisRenderer,
                  tickInterval:'1 day',   // 1000*60*60 = 3600000 = 1 hora em milesegundos,  (javascript timestamps em millisecondos)
                  tickOptions:{formatString:"%d.%m.%y %H:%M", angle: -90},
                  labelOptions: {
                    fontFamily: 'Georgia, Serif',
                    fontSize: '10pt'
                }
              },
              yaxis:{
                label:'',
                labelRenderer: $.jqplot.CanvasAxisLabelRenderer,
                labelOptions: {
                  fontFamily: 'Georgia, Serif',
                  fontSize: '10pt'
                }
              }
          },
          seriesColors:['rgba(153,204,255,1)'],
          series:[{
              lineWidth:1,
              showMarker: true
          }],
          highlighter: {
              showMarker:false,
              tooltipAxes: 'xy',
              yvalues: 2,
              formatString:'<table class="jqplot-highlighter"> \
                                   <tr><td>Data:</td><td>%s</td></tr> \
                                   <tr><td>Uso:</td><td>%s%</td></tr> \
                                   </table>'
          }
      });

      // =============

  });

function lineup(plot, name) {
    var co = plot.plugins.canvasOverlay;
    var line = co.get(name);
    line.options.y += 5;
    co.draw(plot);
}

function linedown(plot, name) {
    var co = plot.plugins.canvasOverlay;
    var line = co.get(name);
    line.options.y -= 5;
    co.draw(plot);
}
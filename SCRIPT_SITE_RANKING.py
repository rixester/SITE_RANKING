import requests
import zipfile
import pandas as pd
import os
import datetime
import datetime as dt
from lxml import etree
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.ticker as ticker

# Gerar a data de hoje e de ontem
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

Ranking_Diario_dir = './Ranking_Diario'
if not os.path.exists(Ranking_Diario_dir):
    os.makedirs(Ranking_Diario_dir)

# Nomes dos arquivos
today_filename = f'./Ranking_Diario/ranking_global_{today}.csv'
yesterday_filename = f'./Ranking_Diario/ranking_global_{yesterday}.csv'

#url = "http://www.tibiame.com/download/scores.zip"
#local_filename = "scores.zip"
# Envia uma solicitação GET para o URL
#response = requests.get(url)
# Verifica se a solicitação foi bem-sucedida (código 200)
#if response.status_code == 200:
#    # Abre um arquivo local para escrita em modo binário
#    with open(local_filename, 'wb') as file:
#        # Escreve o conteúdo do arquivo baixado no arquivo local
#        file.write(response.content)
#    print("Download concluído com sucesso.")
#else:
#    print("Erro ao baixar o arquivo. Código de status:", response.status_code)
#
##-----------------------------------------
# Caminho para o arquivo zip que você baixou
#zip_file_path = 'scores.zip'
# Local onde você quer extrair os arquivos
#extract_to_path = './extracted_files'
# Abre o arquivo zip no modo de leitura
#with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#    # Extrai todos os arquivos no diretório especificado
#    zip_ref.extractall(extract_to_path)
#print("Arquivos extraídos com sucesso.")
##-----------------------------------------
# Carregar o XML
#xml_file_path = './extracted_files/scores.xml'
#with open(xml_file_path, 'rb') as xml_file:
#    xml_doc = etree.parse(xml_file)
# Extrair os dados
#data = []
# Criar dicionário aninhado para as guildas por mundo
#guilds_data = {}
#for world in xml_doc.xpath('//world'):
#    world_id = world.get('id').zfill(2)
#    guilds_data[world_id] = {}
#    for guild in world.xpath('.//guilds/guild'):
#        guild_name = guild.get('name')
#        guild_exp = guild.xpath('.//exppoints/text()')[0]
#        guild_rank = guild.xpath('.//rank[@type="guild"]/text()')
#        guild_rank = guild_rank[0] if guild_rank else 'No Rank'
#        guilds_data[world_id][guild_name] = {'exp': guild_exp, 'rank': guild_rank}
#
# Extrair os dados dos personagens
#data = []
#for world in xml_doc.xpath('//world'):
#    world_id = world.get('id').zfill(2)
#    for character in world.xpath('.//character'):
#        # Seus dados existentes
#        name = character.get('name')
#        level = character.xpath('.//level/text()')[0]
#        vocation = character.xpath('.//vocation/text()')[0]
#        exppoints = int(character.xpath('.//exppoints/text()')[0])
#        achievement = character.xpath('.//achievement/text()')[0]
#        # Verificação da guilda
#        guild = character.xpath('.//guild/text()')
#        guild = guild[0] if guild else ' '

#        # Verificação da quota
#        quota_list = character.xpath('.//quota/text()')
#        quota = quota_list[0] if quota_list else ' '
#
#        # Verificações de rank
# #       highscore_global = next((rank.text for rank in character.xpath('.//rank[@type="highscore_global"]')), 'No rank')
#        highscore_vocation = next((rank.text for rank in character.xpath('.//rank[@type="highscore_' + vocation + '"]')), 'No rank')
#        achievement_global = next((rank.text for rank in character.xpath('.//rank[@type="achievement_global"]')), 'No rank')
#        achievement_vocation = next((rank.text for rank in character.xpath('.//rank[@type="achievement_' + vocation + '"]')), 'No rank')
#        pvp = next((rank.text for rank in character.xpath('.//rank[@type="pvp"]')), 'No rank')
#
#        # Verificação da guilda
#        world_guilds = guilds_data.get(world_id, {})
#        guild_exp = world_guilds.get(guild, {}).get('exp', '0')
#        guild_rank = world_guilds.get(guild, {}).get('rank', '0')
#
#        # Adiciona os dados à lista
#        data.append([
#            world_id, exppoints, name, level, vocation, achievement, guild, quota,
#            highscore_global, highscore_vocation, achievement_global, achievement_vocation, pvp,
#            guild_exp, guild_rank
#        ])
#
## Criar DataFrame
#df = pd.DataFrame(data, columns=['World', 'ExpPoints', 'Name', 'Level', 'Vocation', 'Achievement', 'Guild', 'Quota', 'Highscore Global', 'Highscore Vocation', 'Achievement Global', 'Achievement Vocation', 'PVP', 'Guild Exp', 'Guild Rank'])
#
## Ordenar por ExpPoints em ordem decrescente
#df = df.sort_values(by='ExpPoints', ascending=False)
#
## Adicionar a coluna 'Ranking Global'
#df['Ranking Global'] = range(1, len(df) + 1)
#
## Reorganizar as colunas
#df = df[['World', 'Ranking Global', 'ExpPoints', 'Name', 'Level', 'Vocation', 'Achievement', 'Guild', 'Quota', 'Highscore Global', 'Highscore Vocation', 'Achievement Global', 'Achievement Vocation', 'PVP', 'Guild Exp', 'Guild Rank']]
#
#df = pd.DataFrame(df, columns=['World', 'Ranking Global', 'ExpPoints', 'Name', 'Level', 'Vocation', 'Achievement', 'Guild', 'Quota', 'Highscore Global', 'Highscore Vocation', 'Achievement Global', 'Achievement Vocation', 'PVP', 'Guild Exp', 'Guild Rank'])
#
## Adicionar as novas colunas de cálculos
#df['In Arena'] = df['ExpPoints'] * 0.02
#df['PVP Premium'] = df['ExpPoints'] * 0.05
#df['PVP Free'] = df['ExpPoints'] * 0.10
#df['Insurance 50%'] = df['ExpPoints'] * 0.05
#df['Insurance 80%'] = df['ExpPoints'] * 0.02
#df['Insurance 100%'] = 0
#df['Date'] = today
#
## Criar uma coluna com ExpPoints formatada
#df['Exp Points'] = df['ExpPoints'].apply(lambda x: "{:,}".format(x).replace(',', '.'))
#
## Converter os valores formatados em strings para as novas colunas
#for col in ['In Arena', 'PVP Premium', 'PVP Free', 'Insurance 50%', 'Insurance 80%', 'Insurance 100%']:
#    df[col] = df[col].apply(lambda x: "{:,.0f}".format(x).replace(',', '.'))
#
## Carregar o arquivo ExpTable.csv
#exp_table_df = pd.read_csv('ExpTable.csv')
#
## Certifique-se de que a coluna 'Level' é do tipo inteiro
#exp_table_df['Level'] = exp_table_df['Level'].astype(int)
#df['Level'] = df['Level'].astype(int)
#
## Função para buscar a experiência para o próximo nível
#def get_exp_for_next_level(level):
#    # Verifica se o nível seguinte está no DataFrame
#    if level + 1 in exp_table_df['Level'].values:
#        return exp_table_df[exp_table_df['Level'] == level + 1]['Experience'].iloc[0]
#    else:
#        return None
#def get_exp_for_ToUPl(level):
#    # Verifica se o nível seguinte está no DataFrame
#    if level + 1 in exp_table_df['Level'].values:
#        return exp_table_df[exp_table_df['Level'] == level + 1]['ToUP'].iloc[0]
#    else:
#        return None
## Calcula a experiência necessária para subir de nível
#df['Exp to Up'] = df['Level'].apply(get_exp_for_next_level) - df['ExpPoints']
#
## Calcula a porcentagem para subir de nível
#df['% to Up'] = df['Exp to Up'] / df['Level'].apply(get_exp_for_ToUPl)
#
## Ajustar a porcentagem para formato mais legível
#df['% to Up'] = df['% to Up'].apply(lambda x: round(x * 100, 1) if x is not None else None)
#
######
## Salvar o DataFrame em CSV
#df.to_csv(f'./Ranking_Diario/ranking_global_{today}.csv', index=False)

jogadores_dir = './Jogadores'
if not os.path.exists(jogadores_dir):
    os.makedirs(jogadores_dir)

# ... [Seu código anterior]

# Iterar sobre cada linha do DataFrame
# Define a data de hoje
# Define a data de hoje
today = dt.datetime.now().strftime('%Y-%m-%d')

# Iterar sobre cada linha do DataFrame
#for index, row in df.iterrows():
#    # Construir o nome do arquivo
#    filename = f"./Jogadores/{row['World']}_{row['Name']}.csv"
#
#    # Adicionar a coluna 'Date' com a data de hoje
#    row['Date'] = today
#
#    # Verificar se o arquivo já existe
#    if os.path.exists(filename):
#        # Se existir, ler o arquivo existente
#        df_existing = pd.read_csv(filename)
#
#        # Verificar se a coluna 'Date' existe e converter valores para string
#        if 'Date' in df_existing:
#            df_existing['Date'] = df_existing['Date'].astype(str)
#
#            # Checar se a primeira data é diferente de hoje
#            if df_existing['Date'].iloc[0] != today:
#                #print(f"Adicionando dados para {row['Name']} em {filename}")
#
#                # Criar um novo DataFrame com a linha atual
#                new_row_df = pd.DataFrame([row])
#
#                # Concatenar o DataFrame existente com a nova linha
#                df_updated = pd.concat([new_row_df,df_existing], ignore_index=True)
#
#                # Salvar o DataFrame atualizado no arquivo
#                df_updated.to_csv(filename, index=False)
#    else:
#        # Se não existir, criar um novo DataFrame e salvar como CSV
#        pd.DataFrame([row]).to_csv(filename, index=False)
################################

# Caminho da pasta onde os arquivos CSV são armazenados
# Caminho da pasta onde os arquivos CSV são armazenados
folder_path = './Jogadores'

# Lista todos os arquivos na pasta
file_list = os.listdir(folder_path)

# Processa cada arquivo CSV
# Processa cada arquivo CSV
#for file in file_list:
#    if file.endswith('.csv'):
#        # Constrói o caminho completo para o arquivo
#        file_path = os.path.join(folder_path, file)
#        print(file_path)
#        # Lê o arquivo CSV
#        df = pd.read_csv(file_path)
#
#        # Calcula a diferença invertida de 'ExpPoints'
#        exp_points_diff = df['ExpPoints'].diff(-1)
#
#        # Define o último valor como 0 (ou outro valor padrão que você escolher)
#        exp_points_diff.iloc[-1] = 0
#
#        # Atualiza a coluna 'Gain/Lost Exp' com os novos valores calculados
#        df['Gain/Lost Exp'] = exp_points_diff
#
#        # Salva o DataFrame atualizado no arquivo CSV
#        df.to_csv(file_path, index=False)
#        #####
#
#
# Percorrendo todos os arquivos no diretório
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        filepath = os.path.join(folder_path, filename)

        if filename == "37_Rixestopbr.csv":
            print("....filepath...")
            print(filepath)
            # Lendo o arquivo CSV
            df = pd.read_csv(filepath)
            #print(df)
            #markers = {' ': 'nothing', '': 'nothing', '*': 'star', '+': 'plus', ',': 'pixel', '.': 'point',
            #           '1': 'tri_down', '2': 'tri_up', '3': 'tri_left', '4': 'tri_right', '8': 'octagon',
            #           '<': 'triangle_left', '>': 'triangle_right', 'D': 'diamond', 'H': 'hexagon2', 'None': 'nothing',
            #           'P': 'plus_filled', 'X': 'x_filled', '^': 'triangle_up', '_': 'hline', 'd': 'thin_diamond',
            #           'h': 'hexagon1', 'none': 'nothing', 'o': 'circle', 'p': 'pentagon', 's': 'square',
            #           'v': 'triangle_down', 'x': 'x', '|': 'vline', 0: 'tickleft', 1: 'tickright', 10: 'caretupbase',
            #           11: 'caretdownbase', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright', 6: 'caretup',
            #           7: 'caretdown', 8: 'caretleftbase', 9: 'caretrightbase'}
            # Criando um gráfico
            plt.figure(figsize=(12, 3))

            # Criando um subplot
            ax = plt.subplot(1, 1, 1)  # 1 linha, 1 coluna, 1º subplot

            # Plotando as linhas com cores específicas
            ax.plot(df['Date'], df['ExpPoints'], marker='o')

            # Adicionando linhas de grade
            ax.grid(True, which='both', axis='both', linestyle='--', linewidth=0.5)

            # Ajustar o formato dos números no eixo y
            ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))

            #ax.set_xlabel('Days')
            ax.set_ylabel('Experience')
            plt.xticks(rotation=45)
            plt.tight_layout()

            # Salvando o gráfico como imagem
            graph_name = f"{filename.split('.')[0]}_progress.png"
            plt.savefig(os.path.join(folder_path, graph_name))
            plt.close()



            plt.figure(figsize=(12, 3))
            for i in range(0, len(df)):
                
                color = 'red' if df['Gain/Lost Exp'][i] <= 0 else 'green'
                plt.subplot(1, 1, 1).plot(df['Date'][i - 0:i + 2], df['Gain/Lost Exp'][i - 0:i + 2], color=color, marker='o')
                
            
            # Adicionando linhas de grade
            plt.subplot(1, 1, 1).grid(True, which='both', axis='both', linestyle='--', linewidth=0.5)
            plt.subplot(1, 1, 1).yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
            #plt.xlabel('Days')
            plt.ylabel('Gain/Lost Exp')
            plt.xticks(rotation=45)
            plt.tight_layout()

            # Ajustar limites do eixo Y, se necessário
            y_min = min(df['Gain/Lost Exp']) # Obtém o valor mínimo
            print(y_min)
            y_max = max(df['Gain/Lost Exp']) # Obtém o valor máximo
            print(y_max)
            plt.ylim([y_min - 2 * abs(y_min), y_max + 0.2 * abs(y_max)])

            # Salvando o gráfico como imagem
            graph_name2 = f"{filename.split('.')[0]}_progress2.png"
            plt.savefig(os.path.join(folder_path, graph_name2))
            plt.close()

            # Supondo que df é o seu DataFrame
            character_data = df.iloc[0]

            percent_to_level_up = character_data['% to Up']
            exp_to_level_up = character_data['Exp to Up']
            level_up = character_data['Level'] + 1

            plt.figure(figsize=(8, 0.3)) # Tamanho do gráfico
            bar = plt.barh(' ', percent_to_level_up, color='skyblue')

            # Adicionando o valor da Exp no centro da barra
            for rect in bar:
                width = rect.get_width()
                plt.text(1, rect.get_y() + rect.get_height()/2, f'{exp_to_level_up} exp to UP {level_up}', ha='left', va='center')
                plt.text(width/2, rect.get_y() + rect.get_height()/2, f'{percent_to_level_up}%', ha='center', va='center')

            plt.xlim(0, 100)  # Limite x para 100%

            # Salvando o gráfico como imagem
            graph_name3 = f"{filename.split('.')[0]}_progresso_nivel.png"
            plt.savefig(os.path.join(folder_path, graph_name3))
            plt.close()


            # Extraindo os primeiros valores
            first_values = df[['World', 'Ranking Global', 'Name', 'Level', 'Vocation', 'Achievement', 'Guild', 'Quota', 'Highscore Global', 'Highscore Vocation', 'Achievement Global', 'Achievement Vocation', 'PVP', 'Guild Exp', 'Guild Rank', 'In Arena', 'PVP Premium', 'PVP Free', 'Insurance 50%', 'Insurance 80%', 'Insurance 100%']].iloc[0]
            # Selecionando as colunas desejadas
            selected_data = df[['Date', 'Level', 'ExpPoints', 'Gain/Lost Exp']]
            # Redefinindo o índice
            selected_data.reset_index(drop=True, inplace=True)
            # Convertendo o DataFrame em uma tabela HTML
            html_table = selected_data.to_html(index=False)

            print(html_table)

            def color_gain_loss(val):
                
                color = 'pink' if val < 0 else '#c2faa7'
                return f'background-color: {color}'
            
            styled_html = selected_data.style.format({'Gain/Lost Exp': '{:,.0f}'}) \
                        .applymap(color_gain_loss, subset=['Gain/Lost Exp']) \
                        .to_html(index=False)
            
            print(styled_html)
            style = '''<style>// Centraliza a tabela na página //
                .myTable {
                    margin-left: auto;
                    margin-right: auto;
                }
                
                #myTable {
                width: 50%;
                text-align: center;
                vertical-align: middle;
                }
                #myTable th, #myTable td {
                text-align: center;
                vertical-align: middle;
                }
                
                /* Centraliza o texto dentro da tabela */
                th, td {
                    text-align: center;
                }

                /* Estilos adicionais para a tabela */
                table {
                    border-collapse: collapse;
                    width: 50%; /* Ajuste a largura conforme necessário */
                }

                th, td {
                    padding: 8px;
                    border: 1px solid black;
                }

                th {
                    background-color: #f2f2f2;
                }
                    
                        /* Estilos para os inputs */
                input[type="text"] {
                    width: 50%; /* Ajuste a largura conforme necessário */
                    padding: 8px;
                    text-align: center; /* Centraliza o texto dentro do input */
                }

                /* Estilo para centralizar o texto do placeholder */
                ::placeholder {
                    text-align: center;
                    opacity: 1; /* Ajuste a opacidade conforme necessário */
                }</style>'''

            # Criando um HTML para o arquivo
            html_string = f'''
            <html>
            <head>
                {style}

            <title>Relatório - {filename.split('.')[0]}</title>
            </head>
            <body>
            <center>
            <table align="center" border="5" style="text-valign: center;" valign="MIDDLE" width="50%"><tbody><tr>
            <td colspan=3 align="center">{first_values['Name']}<br><img width="100%"  src='{graph_name3}'></td></tr>
            <tr align="center"><td><p><strong>World:<br></strong> {first_values['World']}</p></td><td><p><strong>Vocation:</strong><br>{first_values['Vocation']}</p></td><td><p><strong>Level:<br></strong> {first_values['Level']}</p></td></tr>
            <tr align="center"><td rowspan=4 align="center"><h1>DIES</h1></td><td><p><strong>PVP</strong></p></td><td><p><strong>INSURANCE</strong></p></td></tr>
            <tr align="center"><td><strong>In Arena:<br></strong>{first_values['In Arena']}</td><td><strong>Insurance 80%:</strong><br>{first_values['Insurance 80%']}</td></tr>
            <tr align="center"><td><strong>PVP Premium:<br></strong>{first_values['PVP Premium']}</td><td><strong>Insurance 50%:</strong><br>{first_values['Insurance 50%']}</td></tr>
            <tr align="center"><td><strong>PVP Free:<br></strong>{first_values['PVP Free']}</td><td><strong>Insurance 100%:</strong><br>{first_values['Insurance 100%']}</td></tr>
            <tr align="center"><td rowspan=3 align="center"><h1>GUILD</h1></td><td><p><strong>PVP</strong></p></td><td><p><strong>INSURANCE</strong></p></td></tr>
            <tr align="center"><td><strong>Guild name:<br></strong>{first_values['Guild']}</td><td><strong>Guild Rank:</strong><br>{first_values['Guild Rank']}</td></tr>
            <tr align="center"><td colspan=2 ><strong>Guild Exp:<br></strong>{first_values['Guild Exp']}</td></tr>
            <tr align="center"><td rowspan=1 align="center"><h1>ACHIEVEMENTS</h1></td><td><strong>Achievement_global:</strong><br>{first_values['Achievement Global']}</td><td><strong>Achievement Vocation:</strong><br>{first_values['Achievement Vocation']}</td></tr>
            <tr align="center"><td rowspan=1 align="center"><h1>PVP</h1></td><td><strong>Quota:</strong><br>{first_values['Quota']}</td><td><strong>PVP Rank:</strong><br>{first_values['PVP']}</td></tr>
            <tr align="center"><td rowspan=1 align="center"><h1>RANKS</h1></td><td><strong>Highscore Global:</strong><br>{first_values['Highscore Global']}</td><td><strong>Highscore Vocation:</strong><br>{first_values['Highscore Vocation']}</td></tr>
            </tbody></table>

            <!-- Adicione mais informações de PVP conforme necessário -->
            <img src='{graph_name}' alt='ExpPoints Progress'><br>
            <img src='{graph_name2}' alt='ExpPoints2 Progress'>
            
            { styled_html }
            
            </body>
            </html>
            '''
            
            #Salvando o HTML
            with open(os.path.join(folder_path, f"{filename.split('.')[0]}.html"), 'w') as f:
                f.write(html_string)

print("Arquivos HTML criados com sucesso.")

###############################



# Converter o DataFrame em HTML e salvar
#html_content = df.to_html(index=False)
#with open(f'{today_filename}.html', 'w', encoding='utf-8') as file:
#    file.write(html_content)

#####

# Aqui você pode fazer mais operações com o DataFrame ou salvá-lo, por exemplo:
#df.to_csv('output2.csv', index=False)
# Exibir a tabela
#print(df)
#df.to_csv('filename.csv', index=False)

# Início do HTML com script para filtragem
#html_start = '''
#<head>
#  <meta charset="UTF-8">
#  <title>Tabela com Filtros e Cópia de Valor</title>
#  <script>
#    function filterTable() {
#      // Obtém os valores dos filtros
#      var filter1 = document.getElementById("filter1").value.toUpperCase();
#      var filter2 = document.getElementById("filter2").value.toUpperCase();
#      var filter3 = document.getElementById("filter3").value.toUpperCase();
#      var filter4 = document.getElementById("filter4").value.toUpperCase();
#      var filter5 = document.getElementById("filter5").value.toUpperCase();
#      var filter6 = document.getElementById("filter6").value.toUpperCase();
#      // Obtém a tabela e suas linhas
#      var table = document.getElementById("myTable");
#      var rows = table.getElementsByTagName("tr");
#      // Loop através de todas as linhas e esconde aquelas que não correspondem aos filtros
#      for (var i = 1; i < rows.length; i++) {
#        var cells = rows[i].getElementsByTagName("td");
#        var col1 = cells[0].textContent.toUpperCase();
#        var col2 = cells[3].textContent.toUpperCase();
#        var col3 = cells[4].textContent.toUpperCase();
#        var col4 = cells[5].textContent.toUpperCase();
#        var col5 = cells[6].textContent.toUpperCase();
#        var col6 = cells[7].textContent.toUpperCase();
#        if (col1.indexOf(filter1) > -1 && 
#			col2.indexOf(filter2) > -1 && 
#			col3.indexOf(filter3) > -1 && 
#			col4.indexOf(filter4) > -1 && 
#			col5.indexOf(filter5) > -1 && 
#			col6.indexOf(filter6) > -1) 
#			{
#          rows[i].style.display = "";
#        } else {
#          rows[i].style.display = "none";
#        }
#      }
#      // Mostra a informação filtrada na primeira linha da tabela
#      var filtered = document.getElementById("filtered");
#      filtered.textContent = "Filtrado por: " + filter1 + ", " + filter2 + ", " + filter3;
#    }
#  </script>
#  <style>
#        // Centraliza a tabela na página //
#        .myTable {
#            margin-left: auto;
#            margin-right: auto;
#        }
#        
#    #myTable {
#        width: 100%;
#        text-align: center;
#        vertical-align: middle;
#        }
#    #myTable th, #myTable td {
#        text-align: center;
#        vertical-align: middle;
#        }
#        
#        /* Centraliza o texto dentro da tabela */
#        th, td {
#            text-align: center;
#        }
#
#        /* Estilos adicionais para a tabela */
#        table {
#            border-collapse: collapse;
#            width: 80%; /* Ajuste a largura conforme necessário */
#        }
#
#        th, td {
#            padding: 8px;
#            border: 1px solid black;
#        }
#
#        th {
#            background-color: #f2f2f2;
#        }
#		
#		    /* Estilos para os inputs */
#        input[type="text"] {
#            width: 100%; /* Ajuste a largura conforme necessário */
#            padding: 8px;
#            text-align: center; /* Centraliza o texto dentro do input */
#        }
#
#        /* Estilo para centralizar o texto do placeholder */
#        ::placeholder {
#            text-align: center;
#            opacity: 1; /* Ajuste a opacidade conforme necessário */
#        }
#    </style>
#  
#</head>
#<body>
#<div style="text-align: center;"><h1>Mundos Tibiame</h1>
#<table align="CENTER" border="5" style="text-valign: CENTER;" valign="MIDDLE" width="100%">
# <thead><tr>
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_1_data.html';">Mundo 1</button></th>  
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_2_data.html';">Mundo 2</button></th>  
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_7_data.html';">Mundo 7</button></th>  
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_9_data.html';">Mundo 9</button></th>  
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_11_data.html';">Mundo 11</button></th>
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_15_data.html';">Mundo 15</button></th>
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_23_data.html';">Mundo 23</button></th></tr>
#    <tr>
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_32_data.html';">Mundo 32</button></th>
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_33_data.html';">Mundo 33</button></th>
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_34_data.html';">Mundo 34</button></th>
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_35_data.html';">Mundo 35</button></th>
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_36_data.html';">Mundo 36</button></th>
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_37_data.html';">Mundo 37</button></th>
#    <th><button onclick="window.location.href='https://rixester.github.io/Tibiame_Rankings/world_38_data.html';">Mundo 38</button></th></tr></thead></table>
#  <div style="text-align: center;">
#  <table align="CENTER" border="5" style="text-valign: CENTER;" valign="MIDDLE" width="100%">
#  <thead><tr style="text-align: right;">
#  <th><input type="text" id="filter1" placeholder="World" onkeyup="filterTable()"></th>
#  <th><input type="text" id="filter2" placeholder="Name" onkeyup="filterTable()"></th>
#  <th><input type="text" id="filter3" placeholder="Level" onkeyup="filterTable()"></th>
#  <th><input type="text" id="filter4" placeholder="Vocation" onkeyup="filterTable()"></th>
#  <th><input type="text" id="filter5" placeholder="Achievement" onkeyup="filterTable()"></th>
#  <th><input type="text" id="filter6" placeholder="Guild" onkeyup="filterTable()"><br></th></tr>
#  </thead></table>
#  
#'''
#
## Fim do HTML
#html_end = '''
#   
#'''
#
## Converter o DataFrame para HTML
#html_content_total = df.to_html(index=False, table_id="myTable")
#
## Concatenar tudo para formar o HTML completo
#full_html_content = html_start + html_content_total + html_end
#
## Salvar o HTML completo
#with open('total_data.html', 'w', encoding='utf-8') as file:
#    file.write(full_html_content)
#    #print('Arquivo HTML para o DataFrame completo criado com sucesso.')
#
## Iterar sobre cada mundo e criar arquivos HTML separados
#for world_id in df['World'].unique():
#    # Formatar o world_id para dois dígitos
#    formatted_world_id = world_id.zfill(2)
#
#    # Filtrar o DataFrame para apenas o mundo atual
#    df_world = df[df['World'] == world_id]
#
#    # Converter o DataFrame filtrado em HTML
#    html_content = df_world.to_html(index=False, table_id="myTable", border=5)
#    full_html_content = html_start + html_content + html_end
#
#    # Criar um arquivo HTML para cada mundo na pasta raiz!
#    with open(f'world_{formatted_world_id}_data.html', 'w', encoding='utf-8') as file:
#        file.write(full_html_content)
#        #print(f'Arquivo HTML para o mundo {formatted_world_id} criado com sucesso.')
#
#
## Criar pastas para cada mundo, se necessário
#for world_id in df['World'].unique():
#    directory = f"./world_data/world_{world_id.zfill(2)}"
#    if not os.path.exists(directory):
#        os.makedirs(directory)
#    print(f'CRIADO PASTAS_world_{world_id.zfill(2)}')
#
##CRIAR UM ARQUIVO CSV PARA CADA MUNDO
#for world_id in df['World'].unique():
#    # Criar um índice booleano para o mundo atual
#    world_index = df['World'] == world_id
#
#    # Usar .loc para adicionar a data de extração diretamente no DataFrame original
#    df.loc[world_index, 'Extraction Date'] = datetime.datetime.now().strftime("%d/%m/%Y")
#
#    # Agora, você pode criar df_world como um novo DataFrame a partir do DataFrame original
#    df_world = df.loc[world_index].copy()
#
#    # Caminho do arquivo
#    file_path = f"./world_data/world_{world_id.zfill(2)}/world_{world_id.zfill(2)}_data.csv"
#
#   # ... [seu código anterior] ...
#
#    # Lógica para Gained/Lost EXP
#    if os.path.exists(file_path):
#        previous_df = pd.read_csv(file_path)
#
#        # Mesclar os DataFrames com base no nome do personagem
#        merged_df = pd.merge(df_world, previous_df, on='Name', suffixes=('_current', '_previous'))
#
#        # Calcular a diferença de EXP
#        merged_df['Gained/Lost EXP'] = merged_df['ExpPoints_current'] - merged_df['ExpPoints_previous']
#
#        # Atualizar df_world com os novos valores de Gained/Lost EXP
#        df_world = pd.merge(df_world, merged_df[['Name', 'Gained/Lost EXP']], on='Name')
#        df_world.to_csv(file_path, index=False)
#    else:
#        # Se o arquivo não existir, basta salvar o DataFrame atual
#        df_world.to_csv(file_path, index=False)
#
#    # ... [continuação do seu código para salvar os arquivos individuais por personagem] ...
#
#    for index, row in df_world.iterrows():
#
#        # Criar um nome de arquivo usando o nome do personagem
#        filename = f"{row['Name']}.csv"
#
#        # Criar um caminho completo para o arquivo
#        # Substitua 'your_directory_path' pelo caminho onde você deseja salvar os arquivos
#        full_path = os.path.join(f"./world_data/world_{world_id.zfill(2)}/", filename)
#        #print(full_path)
#        # Converter a linha do DataFrame em um DataFrame
#        row_df = pd.DataFrame([row])
#
#        # Salvar o DataFrame como um arquivo CSV
#        row_df.to_csv(full_path, index=False)
#        # ... [seu código anterior] ...
#        if os.path.exists(full_path):
#                # Se existir, carregar o arquivo
#                existing_df = pd.read_csv(full_path)
#
#                # Concatenar o DataFrame existente com a nova linha
#                updated_df = pd.concat([existing_df, row_df], ignore_index=True)
#                updated_df.to_csv(full_path, index=False)
#        else:
#                # Se não existir, apenas salvar o DataFrame como um novo arquivo CSV
#                row_df.to_csv(full_path, index=False)
#
#        print("df_world")
#        print(df_world)
def tiles_list(tile_available_movement):
    match tile_available_movement:
        case []:
            tile_top =                  '''         '''
            tile_mid_with_player =      '''         '''
            tile_mid_without_player =   '''         '''
            tile_bot =                  '''         '''
            
        case ['w', 'a', 's', 'd']:
            tile_top =                  '''___| |___'''
            tile_mid_with_player =      '''    ●    '''
            tile_mid_without_player =   '''         '''
            tile_bot =                  '''‾‾‾| |‾‾‾'''

        case ['w', 'a', 'd']:
            tile_top =                  '''___| |___'''
            tile_mid_with_player =      '''    ●    '''
            tile_mid_without_player =   '''         '''
            tile_bot =                  '''‾‾‾‾‾‾‾‾‾'''

        case ['a', 's', 'd']:
            tile_top =                  '''_________'''
            tile_mid_with_player =      '''    ●    '''
            tile_mid_without_player =   '''         '''
            tile_bot =                  '''‾‾‾| |‾‾‾'''

        case ['w', 's', 'd']:
            tile_top =                  '''   | |___'''
            tile_mid_with_player =      '''   |●    '''
            tile_mid_without_player =   '''   |     '''
            tile_bot =                  '''   | |‾‾‾'''

        case ['w', 'a', 's']:
            tile_top =                  '''___| |   '''
            tile_mid_with_player =      '''    ●|   '''
            tile_mid_without_player =   '''     |   '''
            tile_bot =                  '''‾‾‾| |   '''

        case ['s', 'd']:
            tile_top =                  '''    _____'''
            tile_mid_with_player =      '''   |●    '''
            tile_mid_without_player =   '''   |     '''
            tile_bot =                  '''   | |‾‾‾'''

        case ['a', 's']:
            tile_top =                  '''_____    '''
            tile_mid_with_player =      '''    ●|   '''
            tile_mid_without_player =   '''     |   '''
            tile_bot =                  '''‾‾‾| |   '''

        case ['w', 'd']:
            tile_top =                  '''   | |___'''
            tile_mid_with_player =      '''   |●    '''
            tile_mid_without_player =   '''   |     '''
            tile_bot =                  '''    ‾‾‾‾‾'''

        case ['w', 'a']:
            tile_top =                  '''___| |   '''
            tile_mid_with_player =      '''    ●|   '''
            tile_mid_without_player =   '''     |   '''
            tile_bot =                  '''‾‾‾‾‾    '''

        case ['a']:
            tile_top =                  '''_____    '''
            tile_mid_with_player =      '''    ●|   '''
            tile_mid_without_player =   '''     |   '''
            tile_bot =                  '''‾‾‾‾‾    '''

        case ['d']:
            tile_top =                  '''    _____'''
            tile_mid_with_player =      '''   |●    '''
            tile_mid_without_player =   '''   |     '''
            tile_bot =                  '''    ‾‾‾‾‾'''

        case ['w']:
            tile_top =                  '''   | |   '''
            tile_mid_with_player =      '''   |●|   '''
            tile_mid_without_player =   '''   | |   '''
            tile_bot =                  '''   ‾‾‾   '''

        case ['s']:
            tile_top =                  '''   ___   '''
            tile_mid_with_player =      '''   |●|   '''
            tile_mid_without_player =   '''   | |   '''
            tile_bot =                  '''   | |   '''

        case ['a','d']:
            tile_top =                  '''_________'''
            tile_mid_with_player =      '''    ●    '''
            tile_mid_without_player =   '''         '''
            tile_bot =                  '''‾‾‾‾‾‾‾‾‾'''

        case ['w', 's']:
            tile_top =                  '''   | |   '''
            tile_mid_with_player =      '''   |●|   '''
            tile_mid_without_player =   '''   | |   '''
            tile_bot =                  '''   | |   '''

    return tile_top, tile_mid_with_player, tile_mid_without_player, tile_bot
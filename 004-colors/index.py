import segno

qr_simple = segno.make('This is Ante testing')
qr_simple.save('004-colors/ante-with-colors.png', 
                scale=10, 
                border=1, 
                light="grey", 
                dark='#0000ff99', 
                data_dark='darkred'
)
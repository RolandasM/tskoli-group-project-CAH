import pygame

<<<<<<< HEAD
=======
def text_to_screen(screen, text, x, y, size = 49,
            color = (200, 000, 000), font_type = "SansitaOne.tff"):
    try:

        text = str(text)
        #font = pygame.font.Font(font_type, size)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except(Exception, e):
        print('Font Error, saw it coming')
        raise(e)


>>>>>>> master
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top+10
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width-25 and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left+10, y))
        y += fontHeight + lineSpacing+5

        # remove the text we just blitted
        text = text[i:]

    return text

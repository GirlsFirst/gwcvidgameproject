package com.game.src.main;

import java.awt.Graphics;
public class Menu {
  public void render(Graphics g){
    Font fnt0 = new Font("arial, Font.BOLD, 50")
    g.setFont(fnt0)
    g.setColor(Color.white);
    g.drawString("Thana",Game.WIDTh / 2,100)

  }
}

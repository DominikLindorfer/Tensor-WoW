# Tensor-WoW - A Neural-Network playing World of Warcraft

Tensor-WoW is the project behind the program **RotBot**, a fully pixel-based rotation bot for World of Warcraft using a 2D-convolutional neural network based on tensorflow.

<p align="left">
  <img src="https://github.com/DominikLindorfer/Tensor-WoW/assets/21077042/bc5b1ec8-41ab-437e-8178-75d1ebf1254a" width="350">
</p>

## Showcase M+ Video

This demo video shows several high-end M+ keys played using Tensor-WoW from every tank's (my) perspective

[![RotBot Showcase M+](https://i.imgur.com/tDnfpFy.png)](https://vimeo.com/859296819?share=copy "RotBot Showcase M+")

## Supported Classes as of WoW-Patch 10.1.5

Currently supported classes are mainly tanks, which I main :). The respective TF-Lite model for each class, which reads the screen and returns the name of the shown image (according to the icons in [this directory](/WoWIcons/)), can be found [here](./saved_models). The image names are matched to hotkeys as shown below.

| Class  | Spec | Availability |
| ------------- | ------------- | ------------- |
| Death-Knight  | Blood  | ✅  |
| Demonhunter | Vengence  | ✅  |
| Druid | Guardian | ✅  |
| Monk | Brewmaster | ✅  |
| Paladin | Protection & Retribution  | ✅  |
| Warrior | Protection, Arms & Fury  | ✅ |

## Functionality & Usage

The [WoW Addon MaxDps-Minimal](https://github.com/DominikLindorfer/MaxDps-Minimal) is used to show spells and cooldowns for the rotation of each class separately in a customized WeakAura as shown below:

<p align="center">
  <img src="https://github.com/DominikLindorfer/Tensor-WoW/assets/21077042/45f612e4-83bd-4998-b058-cd10ad88dcfd" width="350">
</p>

The respective Weakaura string is:

```sql
!WA:2!fN1AWXXvvApEIDsMeW2YoowoetJHeBJLLTLFgR4kzgPrzMiPzeZmsY2Ybn9J7mDNPNUBD7EK1OTOQefcXKQ4LawGLLcIwETqiadqytGqmcyHWZt0Mn1sXB)ND)f)W1(dQI)SNZT75LKIDIJRnDvtpDFFEUNVZ35EUNo0yD4M5iDFSUpqhL7qRdTZF7lPiRwsJB70NTPn)(dho8iHpq3h5Ik2CngpwqLoBmMPXSZkZ1KYzBB6z4SGNT60mURHT12c9y3iFM0fk4Y8sCHp2n)sp)OJMvXFa0xW))4AfzoBk7uvK5mPbQyAknUUHhRMSLQUnFeBdlpL(INkx8mbDiRXSS1vZ)zFrluOqHZ4QkBYc3tfdTAPln9GrZMKp2aUCzvpuqCpAgxpzUxKygwgErukG)5QhzopUrXIOSU97Kh847BbnMsLcfYv1HXteFOrgy0HI5HVKrUcxUN5CDyMMj1CJCr3kkSPzwEzXwBmtTj7lA2CtMnx0m5IvbNefht5QmEJMncNHnlt2rIp0qzeLOKGjB6PNXsUmZnY8vSceHi8QbQS799)xtUg8Ar)vRFP34cCwrCnrsyMIC7koZlBzuwMwNhf6yaOZyw2wSfzYUSSECMvrp9RFjnu6PwmjTw4UmvBln35O2qJdS3yLLnSW(c7f666H9bDd7hFCllVKDAOnxgBpXqTKCfpeIs7i0WrQvGJleCgL9KdFjF4BaQiAcuY2xM4XtfZ0wwBGyUieU1mLRGMlrIHAu1Tchpsgvtzxx6jfpekT8epIYzbJIrUeAgW4wYMJ5Bz9ObgajTqns45DzMfeMkWnTaTYmcejdRc2CFvtK5f6QKy1B76740DO(SNxcUZexy6B5MFiufdrGBc2eQ)IaBocSLiWTSJ7e26l7SPkUSjftoVcUqvmz5rvYoC6GkxwX1MlGXHT1WkElWTFXML7x2oJ1NSRhSdCrXlY8Qr1hyePd3we4DezoQiYKjpibVn4wHTb3reCYp)gZGkt1sXq9Sn0zgrVG(Zd7aERxSXW0NnA4OdXZVurMfJBOMv3(CPTQ5k(ldtwRkKm)sCuiZsTpfIikJuPCzM5sngeQquuD6SpKdRzFolPr42f5mxxPDl61E8veTnf5NVrFVHo)KoBMAaBgKW1Cm1NNkuSkYhSWC2erjNMLZ3yNusp5AGt(OW9GyNgZv2JSuz6ZXdmZcTasHYim5D3(wHoxcFLCnrWPLMIoZOOU3ekIMZ0HJw4sgfTS5mA(XLVz5mzmmL1HEj7jFPCznqhobvhCxI7hJUFjp2mOGWgNl7qIOZw6BOOdpsU0XgkAFdgT)(tMl5yXvkBW52CDy38G2ppAGyPr9itSHINQFG5CIKK1tbzv2zJQPL2Y9SJZKlffxLUNDyMMH8zZ53x3Z67fCsYlOWjyMZzO5Ppb0teyDKVuK9fBqd1sW6tCVp819u)nYU9qHHddhjJQVt6qjUNhAJIRWWDJ6AndxvoZJnzdTzgzthD5WWgQzu4U0pCkzR3vIdc3Bei6wRHKfvwCY3KBE4D67mPDhch4k7IaPvO8UQmRTiix(mlOpbrISNrAdA)c7egaTuHeb0cSU7B5ec4(HbXEnualagMm8HuqAQJJGwjkvkXGm0yLfY5BYnMomEEy0Tf6C)34WaNQH1gCADWmembzubNfEGjG3nz(atc59nwa5vXYauavaPU7gyqbOiExNaGga08eajnISPCROu5WGXeqP2bOnul6SkkfM5WkhCGXGZeIWY7oIpwa21rauZsk4wqGLvYwwEjic0YuFf9XT6ibP9BafjZ)AdjWn0DyYCPeYwAs4wcgTHkiw8t)lb4I)qUmu5mxZqLLPXBhKg22QuaYGwSOM3uabBO2yog50o8iNzWK5woACvXhUsOXvMx0eniCavXiO8QgnwiBjkUQyYU6VsCJNy8wqHRw7URTqxDSAbbw1phJSJGPdTAmjFSRmHDtF0QLIvkx177qt1e7q7kegwwNEJGyuBydKrmaNXMTngXn8mF5))Hq0YwjCFf7GbQ0wmsBrDo1aNz6PtjFoZc9CTIkmZ6gA9cQqxBDLk(3mQeFFcLqNW2jLmP5j9iPM3j82jL(L1l(EeQNbc0c(AeFTtVRQEXz)n3FoNiendRII4wp7Oj3xgzdTgLsXoo5bR7xbVAOkvIkc3vOj3dPJ3qT0jYnqUC9RWgifbFLB4ApYRt13dDI)()tDpjVPB(cRznHwPNKxBAXRv89xaE35jvFVRq1)kAsA8)2ztIESgr1rQWYHd000X7Q7DEDOMT8mjsusv(y9ZYTsgEOWjUNFWoORBpCGkAnRQZ23yurvVkurvBUTvF2LvK9onZTffeAsm3tVNT1K3kusrpZqrNsoXPpsFrxD3Gp)BLUKQRKU32TJcyJFquj90qNkQvC9SllurbQMhX5bluXsC46DVNis4Lrbjp7IfnXJuGCftM0jpPKhVctYtNzjAbDHbJwHBjQqugZ0LT8klixVqmw6i4pcEqOjJQotTKsfhnmsFcNQ5lxIZ0QGhW3RIBG)ZAyGVpOq(MMHYAh(nm4mhdzx0qfEVxgFS1HPxTor8HP1pY6pYDD8Up2XAayZ5dyPSHdD91D)UHAfYnwv(9N(WXYvnWp7kJ67QW7WExWaDqL1Ucge)BznW6VUDSqWYgpFXmH(cReVSS9KO0AmjZA6U9pPD305ghKvvH2NA1qUDTREBan0)IBM2QYMsQv4CkHi0P)KoP0WYZ0VJB3Ix7T1PST2rZrlJ9QnUkv88Wd)TSH0DIwhNhOTziOhtCWh4Yp(7BFsdzOi5NKOGEjzBzwvY1gnd5Tie62ELyvrzO5y3DcBpuv12mh0Sl7SguUFtpX9X8iaA37PxHPorhLwtD36lPgCG8SNZWHL3zJnr0r9Pb7CX6nHYKMEmYgiVpZ98Dmx90(0XbHul6NsGO(KcKpfyEqBR5C8LzDeiJnSoOHvYMlzzykKZi1VcCH(i8kwISALXZOmtRHxukLi(tt)bIYAHhRgXvzb84hzM161yYLD7ssmmDjfKKK90cgqzkRljsu6ssv21lNb9oTS6TP2fbIGU6JcnmG979KlFaqifHaHrusRc27U(82BJostGKVZSExPtRvtOWwVRD1L0b6s6GRyyeE3wfouD(OB3Unign6BJspP0)qJcPlvDzRImTaXRR2QlycP)AVcN6j3bftckmu3v7nGwtyLILwBvimdoP)QTrfVNvQuQlVD3U817kBqlc5QuBlZ3QuBlI5QOqBzRMELAZMvC5NwwxNBD4ONQ)rYozFPtpu)Php1KJos)rZfVh4rrdyCNUBls9Tz0n0qZvkQG3FpYwvHhF(MSa)9sUujgZjkLrtVmKXUoT5YfDrfCPQ1T)15bzhFDWeNqSFZ53ItNu(JMuCZpJLtAf8aS35Bu3oVdlNnkEZvxgP8nt)9f9lTEAqJfD0CPD2SOqk7HukqvhNsMuSO4RxYFImMHPjk8HxYpDTN2pdZHwuu)dIRAJcvHBAb)CRroDILkDQ4qNC3kkuBwq0q16FGGWZhScS8C24aCJzLExvK1OeclLlNthTi51NPLeLDoBUgLPT5gp4HLAmoI8WNE0CdLmv8G1ElFzGfXAINzYyPZLl9WTnbNQTjGgj67g0zWc9uTTqN2WLsSR(5Vf4lGBP(f35DOcFj)Wo)YW)k8vGVk8Kpm81cbpfgPWxh(giM9nHA(Na4BbFB47ecEA47c)BWZapRZMsMkvdrktY7lro47hcE(8WZTp4heAvaA1gan8atbh9L5y0tuMQPanePpL8RY1BnKr(S2wSKAURDbnJcfmuRy6vLkpghpfJ)d2MIhM3zANMztNoLdzc2mEgUFL90meufxraekgLDS5EyioF05QVbJo0Z2lGrd6hMhxJvqgNz9EWDXQ1sydXi(4IuoILckHJlJ(zUQyusH7Pc3052098CCpX(3)5KlA3TH9(Lh5yz5hEC9u7VN2ctFd1ILiBct(XNwFQcXM12Um9rO6relv5WoBPUOr2M9B4kJWigx2G5Beb2L8dzqQEITfjUV(ldBRH0uwEX52MsXLvg10zoy3hO7dc39wHxuhXcISY0RFGpmorkqTJ6Sn)Cih8Xpe5mnoLlyxDmgU5OVHurmmZxh5WBVWhadIlyA)GWhYpWGqnomZhop8rqhuZRdF0gB3dFmAFE4JlohZ)i8jQV3m8jHpf8zX)PDKFe4Fg(Nwl8zC2CGJpXNKkWRxqAnixFpg8Pfb8t7KtU8Gph84WtupO5f0VQduf(x0HpFlo)Qt6SUQjDW3dEED456ejyiz7AbngUa8dXXOoTLOWcYj8ZfmLFuB0XGJj8te3)3f3xuC)N1YbhEbX9FQ4(pETWVa(Le3cnLG)CEkS))Ko8FcVC9dJiS(GFlsyMIoFW)LVv)Vh(dnmSxmWWwe4cza)7YlyfOT)gQn0GdmRJNLDjEpWFmG2c)AaGxe(n6WlPdlb)hixew)7D7K98VsV1J91X0V0P()c
```

To activate and de-activate the following macro is used (make you own Macro using /m) which triggers a change in color within the above WeakAura and, hence, orders RotBot to continue or stop pressing keys:

```
/stopcasting
/run toggle_single = not toggle_single
```
![image](https://github.com/DominikLindorfer/Tensor-WoW/assets/21077042/f6f6cc13-4e6b-4f3c-aaad-7816a71bc254)

![image](https://github.com/DominikLindorfer/Tensor-WoW/assets/21077042/26b5da8b-a95e-410f-9137-dc8361a40529)

### Configs and Settings

Configs are written in .json format within [this directory](/Config/) and match spells and cooldowns (respectively the names of icons in ) to the correct keybinding, e.g. my Paladin's 'Blessed Hammer' spell is on Hotkey '3' and my 'Ancientkings' cooldown is on 'LSHIFT +  F'.

```
{
    "Class" : "Paladin",
    "Spells" : ["Blessedhammer", "Judgement", "Avengersshield", "Hammerofwrath", "Consecration"],
    "Cooldowns" : ["Ardentdefender", "Sentinel", "Shieldofvengeance", "Acientkings", "Wordofglory", "Seraphim", "Divinetoll", "Eyeoftyr", "Bastionoflight", "Divineshield", "Layonhands", "peacebloom"],
    "Hotkeys Spells" : ["3","1","2","G","Q"],
    "Hotkeys CDs" : [["LALT", "3"], ["LSHIFT", "E"], ["4"], ["LSHIFT", "F"], ["E"],  ["LCONTROL", "3"], ["F"], ["LSHIFT", "3"], ["LALT", "5"], ["LALT", "4"], ["LCONTROL", "4"], []],
    "Hotkey Kick" : [["LSHIFT", "Q"]]
}
```

To read the correct positions from screen, the position of the Weak-Aura needs to be identified. Use RotBot's built in feature to identify the position of the mouse cursor when hovering over the WeakAura on-screen and enter the shown coordinates into the file [settings.py](settings.py). In the example below my spells have their anchor (middle-point) at the coordinates (54, 37) on my screen and 28 is half the pixel-size used in the WeakAura.

<p align="left">
  <img src="https://github.com/DominikLindorfer/Tensor-WoW/assets/21077042/f3a8274d-64a0-4bff-b4e4-1bbcb859b718" width="250">
</p>

```json
"WA_Position_Spells": [
    54,
    37,
    28,
    28
]
```

Use the **Get WA Pictures** button to check, if the icons are visible with entered positions:

<p align="left">
  <img src="https://github.com/DominikLindorfer/Tensor-WoW/assets/21077042/1c69dfb8-1076-471b-b1ea-56d7436914b3" width="200">
</p>



## Screenreading and Keypresses

Spells and cooldowns are read directly from screen using [OpenCV](https://opencv.org/) a simplistic 2D-CNN, as shown below, trained for 10 epochs on 3000 augmented 56x56 images per class ability. The augmentation as well as the training & tests are done within the file [generate_models_CNN.py](generate_models_CNN.py) from which the resulting models are saved using tf-lite (for speed and minimal size). Please note that the augmentation is done b.c. an anchor needs to be defined for screen-reading which, frankly, is difficult to hit pixel-perfect. Hence, a 2D-CNN is a simpler and much more reliable method compared to alternatives like the [structural similarity index measure](https://scikit-image.org/docs/stable/auto_examples/transform/plot_ssim.html), which I've used in previous versions.

```python
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(56, 56, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(len(files)))

model.summary()
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)
history = model.fit(
    train_images, train_labels, epochs=10, validation_data=(test_images, test_labels)
)
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
```

**Keypresses**, following the read spells and cooldowns, are done using [directkeys.py](/lib/directkeys.py) by directly sending the hexcodes for windll.user32.SendInput. The configs to match the keybinds accordingly are defined as jsons in [this directory](/Config/)






# Tensor-WoW - A Neural-Network playing World of Warcraft

Tensor-WoW is the project behind the program **RotBot**, a fully pixel-based rotation bot for World of Warcraft using a 2D-convolutional neural network based on tensorflow.

<p align="left">
  <img src="https://github.com/DominikLindorfer/WoW-RotBot/assets/21077042/cd167c00-0a33-4e63-b318-ea7fbe0b3524" width="350">
</p>

# Demo Video

This demo shows several high-end M+ keys played using Tensor-WoW from every tank's (my) perspective

## Supported Classes as of WoW-Patch 10.1.5

Currently supported classes are mainly tanks, which I main :)

| Class  | Spec | Availability |
| ------------- | ------------- | ------------- |
| Death-Knight  | Blood  | ✅  |
| Demonhunter | Vengence  | ✅  |
| Druid | Guardian | ✅  |
| Monk | Brewmaster | ✅  |
| Paladin | Protection & Retribution  | ✅  |
| Warrior | Protection, Arms & Fury  | ✅ |

# Usage & Functionality

The [WoW Addon MaxDps-Minimal](https://github.com/DominikLindorfer/MaxDps-Minimal) is used to show spells and cooldowns for the rotation of each class separately in a customized WeakAura as shown below:

<p align="center">
  <img src="https://github.com/DominikLindorfer/MaxDps-Minimal/assets/21077042/6f0d528c-e0da-437b-a1c1-16ba74197e89" width="350">
</p>

The respective Weakaura string is:

```sql
!WA:2!fN1AWXXvvApEIDWtfCzlNyKDItA8sILQylBPiNhwysMrAuMjsAgLzgjzB5en9J7mD7PNUBF7EK0OTOQe5qIsQISG2SlbyRLfXJnSKLfgGajB2KScyZgiah0MkbyxE5)S8l(Hl(bvXF4CUDpJMrs5LTPORA6P77ZZ98D(o3Z90HgVn3mhTRJ2vVTvUnT20wyFROiRwsJB70VTPn)Echo8OHpsxh98k2CngpwqLo7iMPXCZjZ1KYzBB6z4SKNT60mURHTv7HEKRGpB6cfCzEjEPN4QETxCSXYQ4pa6lwKBxXjPk2SRSTtUeNve7rUQoSmIkwYVzznMJTLA(p7liHcfkCgxvztw4EQyOvlDPPhkA2K8Xh0LlR6HdI7TMX1tM7fjMHLHxeLc4FU6rM3JBuSikz79M4bp(WlPXuQuOanT8eXhE0bhB4yEKmixHl3Z8UomtZKAUroVBff20mlVSyRnMT2u9hnBUPYMlAMCXQGtIIJPCvgpJLCzMBKmIMQKGjB6P3ORJYzyxZKD04dp8IvSceHi8QbkO76r)Dj3eEDbdlpg3s2CCFT45QjBPQBZh1gRqP)4PYfpZIUmZcIcGo2VH28zS9KPLEmtBzTbJ5IATDNPCfepIedxeQ7gouKmQMYUU0tkEO2ZYJESwbokYz94YEYHVG)enivePsuY2FM4XtTICfpS40ocLBefeYkyumsacfxRiZzNzpBfzotAWkMMstOB4Xw2Vw)122cqWKw4lHxchand)bRMHvbBEzHWhzrzld)hVvyNdcThZY2ITmt2LeqMvrp9RCfneyOwmfbtCxgnwUZtTHKy44XklByH9foo8HUs4oH7cIIpUR1wsBQp3csqVrGBmXln91CvpaQ3HdaDa7aN5iqBrGDfbU6R)MGR51D2zfx2ucmHxbvbkMS84GTpN2OYLvCT5cKEeBnSIRfUUZVA5(LjfRFzxp4gIuJQjWMsh2Bey)WFfSpen4fzEZtvs2s5HDdVp4debN8f2rgezulfdraBO9mI(cdKh2hC9NVXG1VnAnP7lNfzwmUHAwD7zsBLFLwETMR4VmmzTQqY8RWrPolnaPq8wz0kLlZmxPXOsfIYUZE6h51A2Zyjnk3UiN56k1HOxDcXfIQZUO(WMfjFR2t9fPcfcF(fBu67zppjUWC2jXtNMLZNbqkPNEtWnDoOtOdKq6k7rymdxrAgUQCMhBkEG9DOLq2ugHRc39UBO9vWxj)uKldlnfDMrrDVjvenNPd3CHlyu0YMZOjhx3MLZKXWuwhocz77l4RPb6WHP6GUe3piD)cESzrrInbx2HewNRU)HJoYO5shB4O9pu0bgizUKJhxPSbNBZ1HTXdA)IOPILg1JmXgoEQbaMZXss2rfKvzNoQMwAl3tpbtUuuC96E6ryAgYNoNFFDpTpJAkIrjiuqpWTaFqFIrRg3XE7n3HTq(IrpfXgYqTugzthD5WzMXqZtFYmQ(o4dL4oFGDiUcdhnc0D45BO1HTxZOWDO3BkzR7nr3WXIa9T7AiVvLfN8S5Mh2AI76bVIVYFaPriTAd5u7sqR85uq)ckezjJegYoscgejiWD3GwKKmYt0mvaUhyiSxdhy)dJOdPYdPHrP2EVOvHsLsmilnw5OHCI2dnZ)pmMomEDgfCIg2zWj1HYHGjjJi40W9njC)K5cmfK334aK3albqbubK6UnGbfGI4DDO0KbOcQTjLEtOYAkzxRRK6OYIeQinQSPm5sQ7WcS2Sviz71IoNIsHz7vP7bhhoty4uHiysGfG9AqG1033wNCVdaecnsM)DoGG7j4WK5sjKT0Kq)3gTao0W4dnim9Y)M1doN6Yl4Cjqz8bNrSTk1KoUoiHWfcciAuMijJ7yKtR3rp1qjZ1ayU45dKw3x)JaX7w1)szlr7fht2vVvoXNDInKtCrBdF5eRiSVUAFjHAFaogJxZ69Z0qVV9AtFRvlfRuUQ39TC21AXJGcIinihDh(ndg(ZmlO2igO5)GCgBU3eZ)3ZZ(uRdgUiSwVSbdegGk56Wa3hggATk4wS)rORjiA71o7GNA6PtjpJzHEwfdkhY3XeEb3io9Rdd2oQpFyHQPDypKcNabsLIiGe8(f6)3sN4Dkw0dgS28xN(R5JSHRwNdV62X5ebHzyvue97Phl5HYiBO1Ou6Ckt1nuQZlD)jkrfrztASz3YWBDTg1PtKBWC5gqHnyksjVQx(ibMWV3R6L20McTEpjV7uFxU47VcC)5jD(rwNo)n1cJwQTW0J1icosP8ah7p(BfEy3cu63Vh0IHoXxZEzlpBIeLuLVTbyR6Lf1DnupBAdD0(xg1t1lD1ZI9Bxwr27KmxsxeoXD(cxpDTVWcnuvsLn)Z0z70IUjLu0tnC0ZkN4KhT)ORrjT1r36rVJBVRB72cux3vRwtbKXhhvxpd0UIAfxp7YcLfPLqL15CotHkwItA3rNrKWlJcsE2flAINCaPkMmPJFCjpEfMKNoZs0c6cdKVc3suHOmMPlBTvwqUEHyKZrWFeqHGugvDMAjLkoAyC9euvZxUeNcubpTVxf3aNY1WdnCgH8nndL128ByWzng2UOHk8qVfXAuhWEN6djaWUK9kmVpkNYoWr7lEd0Luycqrqw4AOqUXRYVN09glxvO7RKW5McaCHBEjd0jvw7kyy5x3MGTEfx)sbRD8ifZg6lSEqZY2tIs0XumRP7Y)u9DrNrCiwvfABRnc(oWb6Rb(q)lUzARkBkPwHZPuKqN2t64sJip7aoUDjETVMNYwAhnhnn2B04QuXZdpV3Ags3jBECUVwMHGEmz333B94FOdjnSHIKFAJc6LKTLzvjxB0wK3KqOB7vIvfLHvh7Usy7HQQwM5GM9woRbL730JD3mpcG6OZ(e27eNuAt19WVIAWHVZoJHdlVZowfrhZNliTC9MqjIrVvFEejEH2MVEotARBi9Y(jbiQp)aPwbgj0gCo3(ASrcK0g2iKbMKnxYYWuiTrQFf4x9C8kwICDLXZOmtt4tL8AqzfXFAgiqu2m8i1iAllGsJ08Zn7M9Am)YUhusmshukiHjD2eyqPz7GsK0CqjvzxVCg070kRVvvZiIe0vF4OHLSFVNATdaITiwiSMsAvWUJ6ZBFn6inbs(U26B9UW2iHcB9boWbLoYbL6EDdJWx3gqMQtmD7YTbdPrFBu6XL(RBuiDPQlBvKPfiEhSL6cMq6VwRWPEgDqXKqdd1d0AdO1ewPyP1sfclHJ7VABuXhE9kL6YBxTkF9T(g0KqUb1208Tb12KyUbk0M24PpPwmB9TD)iOn6neXpjTUoVVrIEIbgn7u9No9WdKEIutn2Odenx8EQVJJUHgUVcfQWJ2JSvv4XwC1rYFBLluIXCIsPD1ldzSRFrhnX5DriPu16KgDEqI13cm5Xe7xTWv7ShkBttjU5Nj1PScEao(InQB)3OLZoeV5QlJElwnx6N3V065tow0XYL2zxIcPSos5JvDckrrXIIVEb)jYywMMOWhCf)CgFs)e9gAzr9NbvvgfQcDSKFM4i)vXsLovCODUBffQnljAOA9VTq4fdwbwEo7yqUXCs3BfznkR0s5Y50wtsE9zAfrzZyZ1O8Yn)ebpSsJXrKu)0JLB4KPIhS2Bkr6lJ1epZuXsNlx6rAzcorltans0hHypbl0t0YcDAdxkHW6lCnWNhHTVW(Vrv4l6hW6)m8uWxc(xGV8dcpDi4FfJ04Ra)BiM9vHVM)zGQbFD4Bec(MWZaFl4BdpRZotMkvdrktY7oro4Fpe8c5HN)qW)rOnaOvBa0W9Dw4MFDog9f9TtOave5FLCgZ1Bo4t(C2wSKAUBEjnJcfmuRy6vLkpghpeK)d2MIhw0zANv)ob0HKitWvJhI7xzpRgmRIRi2dfJYo2CprWvBlgXyNV(wu6y0w9uHB6CT6EEoUh7WhEg5I2DzyFy5rVTS8ENqp1H7bd0jwISjm53(06NTGin71tb9i2AiJILxeY1zc7C11hyYaBadxzel00vCzLX1DMU76iD1DJaSUGFWds1hlyikTaqPZgBoB7Y032Qh4O7UwtX)OJ6tIWH7QgCS1E3BbmKy)yD5AScYO6tVhCxC4nIroFwMs0Uuq35OGpaZvvhkfweL2T60UFYMd(skICNgNsASRoga3803IQigHAE4vXO5GpkgexW8(4WFJFGbHAC2MpwE4JJ(TwuF9HTVqBWFlTvp8eIZ383b)913Eg(eWtc)J4)0MY4wUFYnJp)PH)bNDf40t8XPc84rX6tUgFe4tjc)p4aspk8zGhd(NQhc9Nv)skNfFUMCLvNczDrtHGNdEbD453dsxqQZLdsj8IWlHJrDsirifun4ve29l3c5k4qdFxX9VN4()P4(l30Xi(Vf3)Ve3)oBg((WpaHB88eVkAGa)680X0(v6WwFO9kiqhD3WBO7BNsNe419Ttrt36M1lhywlIBb(FGxd(j(0Jv0rI0Wdn4CoEw2L49a)uDF7x4Nb)VWBa)CD4xQd)FWVGmp)rWpMmr)H6Ws6Tn9RDI)0p
```

## 

Both spells and cooldowns are read directly from screen using a simplistic 2D-CNN, as shown below, trained for 10 epochs on 3000 augmented 56x56 images per class ability. The augmentation as well as the training & tests are done within the file [generate_models_CNN.py](generate_models_CNN.py) from which the resulting models are saved using tf-lite (for speed and minimal size). Please note that the augmentation is done b.c. an anchor needs to be defined for screen-reading which, frankly, is difficult to hit pixel-perfect. Hence, a 2D-CNN is a simpler and much more reliable method compared to alternatives like the [structural similarity index measure](https://scikit-image.org/docs/stable/auto_examples/transform/plot_ssim.html), which I've used in previous versions.

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







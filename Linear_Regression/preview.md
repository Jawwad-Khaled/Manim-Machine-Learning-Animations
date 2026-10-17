$$n\sum_{i=1}^n{x_i y_i}-\sum_{i=1}^n{y_i}\sum_{i=1}^n{x_i}+\beta_1(\sum_{i=1}^n{x_i})^2-n\beta_1\sum_{i=1}^n{{x_i}^2}=0$$
$$\beta_1=\frac{n\sum_{i=1}^n{x_i y_i}-\sum_{i=1}^n{x_i}\sum_{i=1}^n{y_i}}{{n\sum_{i=1}^n{{x_i}^2}}-(\sum_{i=1}^n{x_i})^2}$$
$$\beta = \begin{bmatrix}\beta_0\\\beta_1\\\vdots\\\beta_p\end{bmatrix}$$
$$\hat{y}=\begin{bmatrix}\beta_0+\beta_1 {x_1}^{(1)}+\cdots+\beta_p {x_p}^{(1)}\\\beta_0+\beta_1 {x_1}^{(2)}+\cdots+\beta_p {x_p}^{(2)}\\\vdots\\\beta_0+\beta_1 {x_1}^{(n)}+\cdots+\beta_p {x_p}^{(n)}\end{bmatrix}$$
$$\nabla{L(\beta_0, \beta_1, \dots, \beta_p)}=\begin{bmatrix}\frac{\partial L}{\partial \beta_0}\\\frac{\partial L}{\partial \beta_1}\\\vdots\\\frac{\partial L}{\partial \beta_p}\end{bmatrix}$$
$$({x_j}^{(i)})^2$$
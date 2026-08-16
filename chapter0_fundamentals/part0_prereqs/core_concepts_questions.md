# 0.0 Prerequisites — Core Concepts questions

---

## Neural Networks

**1. What makes neural networks more powerful than basic statistical methods like linear regression?**

> Neural networks are more powerful than basic statistical methods such as linear regression because they can learn to fit different types of non-linear functions as well as linear ones. 

> Self-feedback: This is done via gradient descent

> Audit: Mark under-specified. The answer earns ARENA's first point (nonlinearity). The self-feedback reads gradient descent as the mechanism that fits the curve, but ARENA's second point is that learning means the model's power is not bounded by algorithms a human could design by hand — the search finds functions nobody could write down. Product, not procedure. Rewrite this line.

> Self-correction: The thing that enables this is gradient descent, adjusting weights to minimise the loss function in multidimensional space. In conclusion, a neural network is more powerful because it uses gradient descent to adjust weights and set features (the type of function). 

**2. What are the advantages of ReLU activations over sigmoids?**

> ReLU activations are simpler to compute than sigmoids and are better suited to navigating the vanishing gradient problem because extreme positive results can still have gradients derived that can be used for the neural network to learn meaningfully, unlike the sigmoid which approaches a gradient of zero in the extremities which neural networks cannot meaningfully learn from. 

> Self-feedback: Well recalled from two weeks ago. 

> Audit: Mark correct. Both of ARENA's points are present — computational cost and vanishing gradients — with the saturation mechanism spelled out, which ARENA's answer only names.

---

## Linear Algebra

**3. What is the problem in trying to create a neural network using only linear transformations?**

> Using only linear transformations to create a neural network limits the amount that the neural network can learn. 

> Self-feedback: True, but this is because the composition of linear transformations cannot create non-linear functions, which is why it is limited. 

> Audit: Mark correct. The original stated the consequence, the self-feedback supplied the mechanism, and the mechanism is exactly ARENA's answer. Note the pattern shared with Q1: consequence written first, mechanism only on the second pass.

**4. Matrices A and B have shapes (n, m) and (m, l). What is the maximum possible rank of the matrix AB?**

> The maximum possible rank of matrix AB is 1 because for any value of n and l, matrix AB will be linearly dependent. 

> Self-feedback: Think this one was well done, but should probably understand the internals of why again. 

> Audit: Mark wrong — the answer is incorrect and was marked as good. ARENA gives rank(AB) <= min(n, m, l). Counterexample to the claim that the maximum is 1: let A and B both be the 2x2 identity, so n = m = l = 2 and AB is the identity, which has rank 2. The error lives in the stated reason, "matrix AB will be linearly dependent" — that phrase needs to be unpacked before re-deriving. UNRESOLVED.

> Self-correction: Matrix rank is the number of dimensions a matrix can reach. For n rows in a matrix, it lives in n dimensional space. Hence, rank(a, b), where a is number of rows and b is number of columns, is lesser than or equal to min(a, b). Take (2, 3), where a < b, thus rank is less than or equal to 2 because you will never need more than two vectors reach all two-dimensional space. Likewise, take (3, 2), where a > b rank is still less than or equal to 2 because you cannot have rank be higher than total number of columns. For matrix AB, rank = min of rank A and rank B, because you cannot access new dimensions using linear combinations. For this question, the new shape of the matrix is (n, l). Its max rank must be the min(l, m, n) because for any matrix multiplication of this type, it cannot access new dimensions.

---

## Probability & Statistics

**5. What is the expected value and variance of the sum of two independent normally distributed random variables X1 ~ N(mu1, sigma1²) and X2 ~ N(mu2, sigma2²)? Are either of these different if they're correlated?**

*(The notebook adds: "We don't necessarily expect you to be able to derive this kind of result.")*

> E(X1 + X2) = E(X1) + E(X2), Var(X1 + X2) = Var(X1) + Var(X2) + 2Cov(X1 + X2)

> Self-feedback: No covariance. Remember that independent implies zero correlation, thus covariance is 0. So technically true, should be simplified to remove the last term. 

> Audit: Mark partly right, and the proposed correction would make the answer worse. The independence point is correct. But the question has two halves, and deleting the covariance term discards the answer to the second one. Keep both cases: independent, the term is zero; correlated, it survives, and its sign is the point — variance larger if correlated, smaller if anticorrelated, mean unchanged either way. The mean-unchanged half and the sign consequence are both missing and both appear in ARENA's answer. Notation: Cov(X1 + X2) should be Cov(X1, X2), since covariance takes two arguments.

---

## Calculus

**6. What is the derivative of quadratic loss L(x, y) = ½(x − y)² with respect to the input x, assuming all variables are scalars rather than vectors?**

**How about for cross entropy loss L(x, y) = −( y·log(x) + (1 − y)·log(1 − x) ), assuming x is in (0, 1) and y is a binary classification label with value either zero or one?**

**What will be the qualitative behaviour of performing gradient descent on x with these loss functions?**

> The derivative of quadratic loss is (x - y)(1 - y dy/dx).
> The derivative of cross entropy loss is -((y/x) + ((y-1)/(1-x)) + y dy/dx(log(x/1-x))).
> Thus the qualitative behaviour of of performing gradient descent on x with these loss functions is that quadratic loss will approaches zero whereas cross entropy loss does not. 

> Self-feedback: Derivation computations are correct, although I'm not sure why the expressions with dy/dx are removed from the solutions. Qualitative behaviour needs to be reviewed. 

> Audit: Mark wrong on the derivations. Two distinct problems. First, y was treated as a function of x — it is a fixed label, so dy/dx is zero, which answers the open question about why the solutions have no dy/dx terms; that alone collapses the quadratic answer to x - y, which is ARENA's. Second, one chain-rule slip made twice: even granting the premise, d/dx of (1/2)(x - y)^2 gives (x - y)(1 - dy/dx), not (x - y)(1 - y dy/dx), and the same spurious y appears in the cross entropy term. Credit where due — strip the dy/dx term and the cross entropy derivative is algebraically identical to ARENA's -y/x + (1 - y)/(1 - x). The qualitative half was correctly flagged; ARENA's answer describes how x moves under the gradient, not whether the loss reaches zero. UNRESOLVED.

> Self-correction: Forgot that implicitly deriving y wrt x also means you have to derive y down to 1. Learnt that in the case of loss functions, x = model output and y = ground truth, thus x - y = total error (error is different from loss in ML). The behavioural difference is that quadratic loss is by design much less sensitive to high errors than cross entropy loss, making cross entropy loss a more efficient loss function for minimising loss from high errors. 

---

## Information Theory

**7. Suppose P is the probability distribution of which word comes next in natural language, and Q is a language model's estimated probability distribution. What will the cross entropy H(P, Q) be if the model is guessing words uniformly? What will the cross entropy be if the model can predict words with the exact right frequency?**

> If the model is guessing words uniformly, the cross entropy of the model would be the entropy of language multiplied by the entropy of the distribution where all words are guessed uniformly. 
> The cross entropy of a model predicting words with the exact right frequency is the entropy of language. 

> Self-feedback: Second response is correct. Need to review the first response. 

> Audit: Mark correct — the second half was rightly called correct and the first rightly flagged. The first half: a uniform Q is a constant, so log Q comes out of the sum, and the remaining sum of P(x) is 1. What survives is the log of the vocabulary size, with no dependence on P at all — not a product of two entropies.

> Self-correction: Start with H(P, Q) = - sum over x of P(x) * log Q(x). If you have a model uniformly picking words, then the log Q(x) = log 1/|v|, where |v| is the amount of vocabulary that the model is selecting from. When every word has a probability of log 1/|v| of selection, the sum over the x multiplying that by the sum over the x of P(x) which always = 1 will equal to log |v|. 

---

## Marking audit — summary

Audited 2026-08-16 against ARENA's answers in `0.0_Prerequisites_exercises.ipynb`.

Marks accurate: Q2, Q3, Q7. Partly accurate: Q1, Q5. Wrong: Q4, Q6.

Both wrong marks run the same direction — wrong work marked correct — and none run the other way. Every question flagged "need to review" (Q3, Q5, Q7) deserved it; every question marked "well done" or "computations are correct" (Q4, Q6) did not. Uncertainty is well calibrated here; confidence is not. Q4 and Q6 are the open items.

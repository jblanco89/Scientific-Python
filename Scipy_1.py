{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Scipy primera clase\n",
    "## Aprendiendo su forma de importación\n",
    "### conociendo algunas funciones integradas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from scipy import integrate\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Función de Campana de Gauss\n",
    "\n",
    "$$f(x) = e^{-x^2}$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "## definimos la ecuación en python\n",
    "def f(x):\n",
    "    return np.exp(-x**2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Aplicamos integración numérica gracias librería integrate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.8862073482595214, 3.1768223732680054e-11)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "integrate.quad(f, 0, 3) ## el primer valor es el resultado de la integral, el segundo es el error resultante"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Ecuaciones Diferenciales (EDO's)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "$$y' + y  = 0$$\n",
    "$$y' = f(y)$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(y,t):\n",
    "    return -y\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "y0 = 1.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "t = np.linspace(0,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "sol = integrate.odeint(f,y0,t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x1f4f73c67c8>]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(t,sol)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Ecuaciones diferenciales con orden mayor a 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "$$y'' + y = 0$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "$$\\mathbf{f}(\\mathbf{y}) = \\pmatrix{y \\\\ y'} = \\pmatrix{y' \\\\ y''} = \\pmatrix{y' \\\\ -y}$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(y,t):\n",
    "    return np.array([y[1],-y[0]])## preguntar ya que no concuerda con la ec."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "t = np.linspace(0,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "y0 = np.array([1.0,0.0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1.        ,  0.        ],\n",
       "       [ 0.97924752, -0.20266792],\n",
       "       [ 0.91785142, -0.39692413],\n",
       "       [ 0.81835993, -0.57470602],\n",
       "       [ 0.68490246, -0.72863476],\n",
       "       [ 0.52301813, -0.85232155],\n",
       "       [ 0.33942597, -0.94063276],\n",
       "       [ 0.14174595, -0.98990306],\n",
       "       [-0.06181722, -0.99808747],\n",
       "       [-0.26281468, -0.96484631],\n",
       "       [-0.45290402, -0.89155926],\n",
       "       [-0.6241956 , -0.78126807],\n",
       "       [-0.76957997, -0.6385504 ],\n",
       "       [-0.88302297, -0.46932972],\n",
       "       [-0.95981615, -0.28062952],\n",
       "       [-0.99677219, -0.0802818 ],\n",
       "       [-0.99235725,  0.12339801],\n",
       "       [-0.94675456,  0.32195619],\n",
       "       [-0.86185686,  0.5071516 ],\n",
       "       [-0.74118783,  0.6712977 ],\n",
       "       [-0.58975583,  0.80758162],\n",
       "       [-0.41384604,  0.9103469 ],\n",
       "       [-0.22075958,  0.97532827],\n",
       "       [-0.01851051,  0.99982868],\n",
       "       [ 0.18450685,  0.98283125],\n",
       "       [ 0.37986625,  0.92504144],\n",
       "       [ 0.55945933,  0.82885784],\n",
       "       [ 0.71583207,  0.69827252],\n",
       "       [ 0.84249423,  0.53870543],\n",
       "       [ 0.93418871,  0.35677939],\n",
       "       [ 0.98710972,  0.16004524],\n",
       "       [ 0.99906079, -0.04333159],\n",
       "       [ 0.96954589, -0.24490994],\n",
       "       [ 0.89979002, -0.43632331],\n",
       "       [ 0.79268841, -0.60962711],\n",
       "       [ 0.65268629, -0.75762836],\n",
       "       [ 0.48559446, -0.87418429],\n",
       "       [ 0.29834805, -0.95445723],\n",
       "       [ 0.09871872, -0.99511547],\n",
       "       [-0.10500794, -0.99447148],\n",
       "       [-0.30437624, -0.952552  ],\n",
       "       [-0.49111143, -0.87109689],\n",
       "       [-0.65746306, -0.75348693],\n",
       "       [-0.79652672, -0.60460354],\n",
       "       [-0.90253057, -0.43062609],\n",
       "       [-0.97107493, -0.23877553],\n",
       "       [-0.99931487, -0.0370146 ],\n",
       "       [-0.98607829,  0.16628263],\n",
       "       [-0.93191456,  0.36267831],\n",
       "       [-0.83907176,  0.54402103]])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sol = integrate.odeint(f,y0,t)\n",
    "sol #herramienta util para diseño de reactores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x1f4f7480c08>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, axes = plt.subplots()\n",
    "axes.plot(t,sol[:,0],label ='Posición')#posición\n",
    "axes.plot(t,sol[:,1], '-r', label='Velocidad')#velocidad\n",
    "axes.legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Ecuaciones algebráicas no lineales\n",
    "### Conociendo la librería optimize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy import optimize"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Probando con la ecuación:\n",
    "$$x^5 + 5x + 1 = 0$$\n",
    "#### volviendola función sería:\n",
    "$$ f(x) = x^5 + 5x + 1$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "#definimos la función en python\n",
    "def f(x):\n",
    "    return x**5 + 5*x + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "    fjac: array([[-1.]])\n",
       "     fun: array([0.])\n",
       " message: 'The solution converged.'\n",
       "    nfev: 6\n",
       "     qtf: array([-4.17332835e-13])\n",
       "       r: array([-5.00798978])\n",
       "  status: 1\n",
       " success: True\n",
       "       x: array([-0.1999361])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "optimize.root(f,0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-0.1999361])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sol = optimize.root(f,0)\n",
    "sol.x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Probando con la ecuación:\n",
    "$$10*e^{t/2}\\cos2t = 4$$\n",
    "#### volvéndola función nos queda:\n",
    "$$f(t) = 10*e^{t/2}\\cos2t - 4$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# definimos la función en python\n",
    "def f(t):\n",
    "    return 10*np.exp(t/2)*np.cos(2*t) - 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.        ,  0.20408163,  0.40816327,  0.6122449 ,  0.81632653,\n",
       "        1.02040816,  1.2244898 ,  1.42857143,  1.63265306,  1.83673469,\n",
       "        2.04081633,  2.24489796,  2.44897959,  2.65306122,  2.85714286,\n",
       "        3.06122449,  3.26530612,  3.46938776,  3.67346939,  3.87755102,\n",
       "        4.08163265,  4.28571429,  4.48979592,  4.69387755,  4.89795918,\n",
       "        5.10204082,  5.30612245,  5.51020408,  5.71428571,  5.91836735,\n",
       "        6.12244898,  6.32653061,  6.53061224,  6.73469388,  6.93877551,\n",
       "        7.14285714,  7.34693878,  7.55102041,  7.75510204,  7.95918367,\n",
       "        8.16326531,  8.36734694,  8.57142857,  8.7755102 ,  8.97959184,\n",
       "        9.18367347,  9.3877551 ,  9.59183673,  9.79591837, 10.        ])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t = np.linspace(0,10)\n",
    "t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x1f4f7509c08>]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(t,f(t))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-0.5136520947507961"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "optimize.bisect(f,-1,0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-0.5136520947508494"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "optimize.newton(f,0)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

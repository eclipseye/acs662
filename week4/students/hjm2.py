import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import confidence_ellipse

# --------------------------data 불러오기----------------------------------------------------------

particle=np.loadtxt('coord.out', skiprows=1, dtype='float')

x = particle[:,4]
x_p=particle[:,5]
y = particle[:,6]
y_p= particle[:,7]


# --------------------------fig를 나누어 sub_plot을 입력할 때---------------------------------------

fig = plt.figure()
fig.subplots_adjust(hspace=0.4,wspace=0.2)
# 상하 좌우 간격 설정
fig.tight_layout()
# 상하 좌우 여백 설정


ax_scatter = fig.add_subplot(2,2,3)
ax_scatter.scatter(x, x_p,s=0.1)

ax_scatter.set_xlabel('x', size='15')
ax_scatter.set_ylabel('x_prime', size='15')


ax_hist_x = fig.add_subplot(2,2,1)
ax_hist_x.hist(x, 20, histtype='step',orientation = 'vertical')
ax_hist_x.set_title('x_histogram')

ax_hist_x_p = fig.add_subplot(2,2,4)
ax_hist_x_p.hist(x_p, 20, histtype='step',orientation = 'horizontal')
ax_hist_x_p.set_title('x_p_histogram')


# GridSpec 명령어를 사용하지 않으면 동일한 크기의 sub-plot이 생성된다. 그래프의 사이즈를 보다 편하게 설정하기 위해서 GridSpec 명령어를 사용.
# --------------------------GridSpec 라이브러리르 사용할 때---------------------------------------

fig2 = plt.figure()
fig2.subplots_adjust(hspace=1,wspace=1)
# fig2.tight_layout()
gs = GridSpec(4, 4)


ax_scatter = fig2.add_subplot(gs[1:4, 0:3])
ax_scatter.scatter(x, x_p,s=0.1)
ax_scatter.set_xlabel('x', size='15')
ax_scatter.set_ylabel('x_prime', size='15')


ax_hist_x = fig2.add_subplot(gs[0,0:3])
ax_hist_x.hist(x, 20, histtype='step', orientation = 'vertical')
ax_hist_x.set_title('x_histogram')

ax_hist_x_p = fig2.add_subplot(gs[1:4, 3])
ax_hist_x_p.hist(x_p, 20, histtype='step', orientation = 'horizontal')
ax_hist_x_p.set_title('x_p_histogram')


# --------------------------normalized coordinate---------------------------------------

alpha_x=0.399
beta_x=0.0109

gamma_x = (1+alpha_x**2)/beta_x
    
x_n = x/np.sqrt(beta_x)
x_p_n = (alpha_x*x+beta_x*x_p)/np.sqrt(beta_x)


fig3 = plt.figure()
fig3.subplots_adjust(hspace=1,wspace=1)
fig3.tight_layout()
gs = GridSpec(4, 4)


ax_scatter = fig3.add_subplot(gs[1:4, 0:3])
ax_scatter.scatter(x_n, x_p_n,s=0.1)
ax_scatter.set_xlabel('x_normalized', size='15')
ax_scatter.set_ylabel('x_prime_normalized', size='15')




ax_hist_x = fig3.add_subplot(gs[0,0:3])
ax_hist_x.hist(x_n, 20, histtype='step', orientation = 'vertical')
ax_hist_x.set_title('x_normalized_histogram')

ax_hist_x_p = fig3.add_subplot(gs[1:4, 3])
ax_hist_x_p.hist(x_p_n, 20, histtype='step', orientation = 'horizontal')
ax_hist_x_p.set_title('x_p_normalized\nhistogram')

plt.show()

# --------------------------x,x_p contour by rms emittance---------------------------------------
# rms emittance 공식을 이용하여 등고선을 이용하여 1~3 시그마의 emittance를 표현
emittance_RMS = np.sqrt(np.mean(x**2)*np.mean(x_p**2)-np.mean(x*x_p)**2)

emittance = gamma_x*x**2+2*alpha_x*x*x_p+beta_x*x_p**2

x_l = np.linspace(np.min(x), np.max(x),1000)
x_p_l = np.linspace(np.min(x_p), np.max(x_p),1000)

X,Y = np.meshgrid(x_l,x_p_l)

emittance = gamma_x*X**2+2*alpha_x*X*Y+beta_x*Y**2

fig4 = plt.figure()
# fig4.subplots_adjust(hspace=1,wspace=1)



ax_0 = fig4.add_subplot(1,2,1)
ax_0.scatter(x, x_p,s=0.1)
ax_0.set_xlabel('x', size='15')
ax_0.set_ylabel('x_prime', size='15')


ax_0.contour(X,Y,emittance,[emittance_RMS],colors='red')
# 1시그마 RMS emittance를 표현
ax_0.contour(X,Y,emittance,[4*emittance_RMS],colors='blue')
# 2시그마 RMS emittance를 표현
ax_0.contour(X,Y,emittance,[9*emittance_RMS])
# 3시그마 RMS emittance를 표현

# --------------------------x,x_p by function ---------------------------------------
# 공분산을 이용하여 신뢰 타원을 그리는 방법을 이용하여 rms emittance를 구하는 방법  

ax_1 = fig4.add_subplot(1,2,2)
ax_1.scatter(x, x_p,s=0.1)
ax_1.set_xlabel('x', size='15')


confidence_ellipse.confidence_ellipse(x, x_p, ax_1, edgecolor='blue')
# 2시그마 RMS emittance를 confidence_ellipse 함수로 표현

plt.show()






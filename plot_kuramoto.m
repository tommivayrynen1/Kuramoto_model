
function plot_kuramoto(t,theta)

    r = 1;
    polarX = r*cos(theta);
    polarY = r*sin(theta);
    z = abs(1/size(theta,2)*sum(exp(1i*theta),2));
    aveX = mean(r*cos(theta),2);
    aveY = mean(r*sin(theta),2);


    figure;subplot(2,4,[1,5]);title('Polar');
    hold on;plot(r*cos([-pi:.01:pi]),r*sin([-pi:.01:pi]),'LineWidth',2,'Color','k');
    for i = 1:length(t)
    subplot(2,4,[1,5]);
    s=scatter(polarX(i,:),polarY(i,:),40,'filled','MarkerFaceColor',[.6 0 0]);xlim([-1.5 1.5]);ylim([-3 3]);
    q=quiver(0,0,aveX(i),aveY(i),'LineWidth',2,'Color','k');
    
    
    subplot(2,4,[2:4]);title('Amplitude');xlabel('Time / s');
    window = 50;
    from = i-window; if from <1; from=1;end
    to = i;
    hold on;
    p=plot(t(from:to),polarY(from:to,:),'LineWidth',2,'Color','k');
    xlim([t(from) t(to+10)]);ylim([-1.5 1.5]);
    s2=scatter(repmat(t(to),1,size(theta,2)),polarY(to,:),40,'filled','MarkerFaceColor',[.6 0 0]);
    
    subplot(2,4,[6:8]);hold on;title('Order parameter \kappa');xlabel('Time / s');
    p2=plot(t(from:to),z(from:to,:),'LineWidth',2,'Color','k');
    xlim([t(from) t(to+10)]);ylim([0 1.2]);
    s3=scatter(t(to),z(to,:),40,'filled','MarkerFaceColor',[.6 0 0]);
   
    drawnow;delete(s);delete(s2);delete(p);delete(p2);delete(s3);delete(q)
    end
    
end

package javabeans;

import javabeans.Enfermaria;
import javabeans.Enfermeiro;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.7.10.v20211216-rNA", date="2022-07-20T19:59:25")
@StaticMetamodel(Alocacao.class)
public class Alocacao_ { 

    public static volatile SingularAttribute<Alocacao, Enfermeiro> enfermeiro;
    public static volatile SingularAttribute<Alocacao, Enfermaria> enfermaria;
    public static volatile SingularAttribute<Alocacao, Long> id;
    public static volatile SingularAttribute<Alocacao, Integer> versao;

}
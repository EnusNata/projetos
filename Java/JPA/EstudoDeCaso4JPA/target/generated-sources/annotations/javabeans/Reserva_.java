package javabeans;

import java.util.Date;
import javabeans.Passageiro;
import javabeans.Voo;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.7.10.v20211216-rNA", date="2022-07-21T15:52:37")
@StaticMetamodel(Reserva.class)
public class Reserva_ { 

    public static volatile SingularAttribute<Reserva, Integer> codigo;
    public static volatile SingularAttribute<Reserva, Date> data_reserva;
    public static volatile SingularAttribute<Reserva, Voo> voo;
    public static volatile SingularAttribute<Reserva, Long> id;
    public static volatile SingularAttribute<Reserva, Passageiro> passageiro;
    public static volatile SingularAttribute<Reserva, Integer> versao;

}